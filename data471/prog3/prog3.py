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
    parser.add_argument("--lr", help="Learning rate for gradient descent.")
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

#Model will be trained to minimize empirical risk w/ squared error loss

#Two different algorithms for finding optimal w and b
# - plugged into a closed-form solution
# - gradient descent algorithm

# Training result is a model file which is
# - plaintext file of a single line containing: 
#  - b: D+1 numbers in scientific notation 1.234e+02 seperated with space
#  - w_1-w_D
#  i.e.
# 3.142e+01 w1 w2 w3 w4
#===================================================================================
def train_model(trainx, trainy, devx, devy, model, lr, max_steps, mb, patience, dev_freq, verbose):
    if steps == 0:
        model = train_analytical(inputs, targets)
    else:
        model = train_gd(inputs, targets, float(lr), steps)
    np.savetxt(model_path, model, fmt="%.3e", newline=" ")
    return

def train_analytical(inputs, targets):
    ones = np.ones(np.shape(inputs)[0])
    features = np.column_stack((ones, inputs))
    inverse = np.dot(np.transpose(features), features)
    try:
        inverse = np.linalg.inv(inverse)
    except np.linalg.LinAlgError:
        sys.exit("Matrix is unable to be inverted")
    
    return np.dot(np.dot(np.transpose(features), targets), inverse)


def train_gd(inputs, targets, lr, steps):
    shape = np.shape(inputs)
    w = np.zeros(shape[1])
    b = 1
    for i in range(steps):
        yHat = (np.dot(inputs, w)+b) - targets
        xT = np.transpose(inputs)
        wGrad = (2/shape[0])*(np.dot(xT, yHat))
        bGrad = (2/shape[0])*np.sum(yHat)
        w = w-lr*wGrad
        b = b-lr*bGrad
    return np.concatenate(([b], w))


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
# using mean/average squared error loss (MSE)
# output: print dev set MSE in scientific notation, 3 decimal places
#===================================================================================
def model_eval(devx, devy, model):
    p = model_predictions(devx, model)
    if np.shape(devx)[0] != np.shape(devy)[0]:
        sys.exit("Input data and target data are not the same length")
    classes = np.argmax(p, axis=1)
    correct = np.sum(classes == devy)
    accuracy = correct / np.shape(devx)[0]
    print(f"{accuracy:.3f}")

def softmax(z):
    expZ = np.exp(z - np.max(z, axis=1, keepdims=True)) 
    return (expZ / np.sum(expZ, axis=1, keepdims=True))

def main():
    args = initialize()

    if args.train:
        # load trainx,y devx,y model, lr, maxsteps, mb, patience, dev_freq, verbose
        trainx = np.atleast_2d(np.load(args.trainx))
        trainy = np.load(args.trainy)
        devx = np.atleast_2d(np.load(args.devx))
        devy = np.load(args.devy)
        train_model(trainx, trainy, devx, devy, args.model, args.lr, args.max_steps, args.mb, args.patience, args.dev_freq, args.verbose)
    elif args.predict:
        model = np.load(args.model)
        devx = np.atleast_2d(np.load(args.devx))
        p = model_predictions(devx, model)
        np.save(args.preds, p)
    elif args.eval:
        devx = np.atleast_2d(np.load(args.devx))
        devy = np.load(args.devy)
        model = np.load(args.model)
        model_eval(devx, devy, model)

if __name__ == "__main__":
    main()