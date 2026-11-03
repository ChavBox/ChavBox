import numpy as np
import argparse
import sys
from pathlib import Path

def initialize():
    parser = argparse.ArgumentParser(usage='%(prog)s [-h] (--train | --predict | --eval) [--trainx TRAINX] [--trainy TRAINY] [--devx DEVX]'
                                                        '[--devy DEVY] [--model MODEL] [--preds PREDS] [--lr LR] [--max-steps MAX_STEPS]' \
                                                        '[--mb MB] [--patience PATIENCE] [--dev_freq DEV_FREQ] [--verbose]',)                       
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--train", action="store_true", help="Train a multinomial logistic regression model from X and Y.")
    mode.add_argument("--predict", action="store_true", help="Run prediction on a dev/test set using a trained model.")
    mode.add_argument("--eval", action="store_true", help="Evaluate a trained model on a dev set (prints accuracy).")

    parser.add_argument('--trainx', default='', help="Path to training inputs npy file.")
    parser.add_argument('--trainy', default='', help="Path to training targets npy file (class labels).")
    parser.add_argument('--devx', default='', help="Path to development inputs npy file.")
    parser.add_argument('--devy', default='', help="Path to development targets npy file (class labels).")
    parser.add_argument("--model", default='model.npz', help="Path to model file to be written (train) or read (predict/eval). default \"model.npz\".")
    parser.add_argument("--preds", help="Path to write predictions npy file(predict).")
    parser.add_argument("--lr", type=float, help="Learning rate for gradient descent.")
    parser.add_argument("--max-steps", type=int, default=5000, help="Max MB-SGD steps, default 5000.")

    parser.add_argument('--mb', type=int, default=32, help="Mini-batch size, default 32.")
    parser.add_argument('--patience', type=int, default=10, help="Early stopping patience in number of dev evals without improvement, default 10.")
    parser.add_argument('--dev_freq', type=int, default=500, help="Evaluate on the dev set every this number of gradient steps, default 500.")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose mode, in which each minibatch loss is printed.")


    args = parser.parse_args()
    if args.train and not (args.trainx and args.trainy and args.devx and args.devy and args.lr):
        parser.error("--train requires the following arguments: --trainx --trainy --devx --devy --lr")
    elif args.predict and not (args.devx and args.preds):
        parser.error("--predict requires the following arguments: --devx --preds")
    elif args.eval and not (args.devx and args.devy):
        parser.error("--eval requires the following arguments: --devx --devy")

    return args

#===================================================================================
#Training mode:
# Takes training set of an N x D matrix of
# inputs and a vector of N_tr outputs
#N: number of training examples
#D: dimensionalyity of each input vector
#Model will be trained to minimize empirical risk w/ cross-entropy loss
# - minibatch stochastic gradient descent algorithm
# Training result is a model file which is
# - binary numpy npz file
#  - b: length c numpy array
#  - W: D x C numpyh array of np.float64
# Usage:
# model =np.load("model.npz")
#W = model["W"]
#b = model["b"]
#===================================================================================
def train_model(trainx, trainy, devx, devy, lr, max_steps, mb, patience, dev_freq, verbose, model):
    N_tr, D = np.shape(trainx)
    N_dev, D_dev = np.shape(devx)
    if mb > N_tr:
        sys.exit(f"Mini-batch size {mb} is larger than training set size {N_tr}")
    if N_tr != np.shape(trainy)[0]:
        sys.exit(f"Training inputs {N_tr} and outputs {np.shape(trainy)[0]} are not the same length")
    if N_dev != np.shape(devy)[0]:
        sys.exit(f"Dev inputs {N_dev} and outputs {np.shape(devy)[0]} are not the same length")
    if D != D_dev:
        sys.exit(f"Training {N_tr} x {D} and dev {N_dev} x {D_dev} data are not the same dimensionality")
    if lr <= 0 or mb <= 0 or max_steps <= 0 or patience <= 0 or dev_freq <= 0:
        sys.exit(f"Learning rate: {lr}, mini-batch size: {mb}, max steps: {max_steps}, patience: {patience}, and dev frequency: {dev_freq} must be positive")
    c = np.max(trainy) + 1
    W = np.zeros((D, c))
    b = np.zeros(c)
    steps = 0
    epoch = 1
    lossChange = 0
    bestLoss = float("inf")
    while steps < max_steps:
        indices = np.random.permutation(N_tr)
        trainx = trainx[indices]
        trainy = trainy[indices]
        for start in range(0, N_tr, mb):
            end = start + mb
            if end > N_tr or steps >= max_steps:
                break
            miniX = trainx[start:end]
            miniY = trainy[start:end]
            p = model_predictions(miniX, {"W": W, "b": b})
            oneHot = np.eye(c)[miniY]
            wGrad, bGrad, risk = miniBatch_SGD(p, oneHot, miniX)
            W = W - lr * wGrad
            b = b - lr * bGrad
            steps += 1
            if verbose:
                print(f"{risk:.3f} batch, update {steps}, epoch {epoch}")
            if steps % dev_freq == 0:
                p = model_predictions(devx, {"W": W, "b": b})
                oneHot = np.eye(c)[devy]
                dev_loss = avg_loss(p, oneHot)
                acc = accuracy(p, devy)
                if dev_loss < bestLoss:
                    np.savez(model, W=W, b=b)
                    bestLoss = dev_loss
                    lossChange = 0
                else:
                    lossChange += 1
                if lossChange > patience:
                    print(f"Early stopping after {steps} updates, epoch {epoch}")
                print(f"dev loss={dev_loss:.3f} acc={acc:.3f} (as of update {steps}, epoch {epoch})")
        epoch += 1

def avg_loss(p, oneHot):
    loss = -np.sum(oneHot * np.log(p), axis=1)
    risk = np.mean(loss)
    return risk

def miniBatch_SGD(p, oneHot, minix):
    risk = avg_loss(p, oneHot)
    xT = np.transpose(minix)
    ones = np.ones(np.shape(oneHot)[0])
    wGrad = (np.dot(xT, (p - oneHot))) / np.shape(minix)[0]
    bGrad = np.dot(np.transpose(ones), (p-oneHot)) / np.shape(minix)[0]
    return wGrad, bGrad, risk



#===================================================================================
#Prediction mode:
# Program takes a trained model, and new set of input
# makes predictions for each input, storing result to a file
# - N x C nd array of type np.float64
# - N is the number of data points
# - C is the number of classes
#===================================================================================
def model_predictions(devx, model):
    W = model["W"]
    b = model["b"]
    d, c = np.shape(W)
    if np.shape(b) != (c,):
        sys.exit("Model file is not in the correct format")
    elif np.shape(devx)[1] != d:
        sys.exit("Input data is not in the correct format")
    z = np.dot(devx, W) + b
    return softmax(z)

#===================================================================================
#Evaluation mode:
# Program takes trained model, and data set to evaluate on
# Dataset:
# - N_dev X D matrix of inputs
# - vector of N_dev outputs
# N_dev: Number of examples
# D: dimensionality of each input vector
# N_dev does not need to equal N_tr
# program will make predictions on dev set inputs
# and evaluate how well predictions match true output
# using accuracy
# output: dev set accuracy
#===================================================================================
def model_eval(devx, devy, model):
    p = model_predictions(devx, model)
    if np.shape(devx)[0] != np.shape(devy)[0]:
        sys.exit("Input data and target data are not the same length")
    return accuracy(p, devy)

def accuracy(p, devy):
    classes = np.argmax(p, axis=1)
    correct = np.sum(classes == devy)
    return correct / np.shape(devy)[0]

def softmax(z):
    expZ = np.exp(z - np.max(z, axis=1, keepdims=True)) 
    return (expZ / np.sum(expZ, axis=1, keepdims=True))

def main():
    args = initialize()

    if args.train:
        trainx = np.atleast_2d(np.load(args.trainx))
        trainy = np.load(args.trainy)
        devx = np.atleast_2d(np.load(args.devx))
        devy = np.load(args.devy)
        train_model(trainx, trainy, devx, devy, args.lr, args.max_steps, args.mb, args.patience, args.dev_freq, args.verbose, args.model)
    elif args.predict:
        model = np.load(args.model)
        devx = np.atleast_2d(np.load(args.devx))
        p = model_predictions(devx, model)
        np.save(args.preds, p)
    elif args.eval:
        devx = np.atleast_2d(np.load(args.devx))
        devy = np.load(args.devy)
        model = np.load(args.model)
        accuracy = model_eval(devx, devy, model)
        print(f"{accuracy:.3f}")


if __name__ == "__main__":
    main()