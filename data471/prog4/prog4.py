import numpy as np
import argparse
import sys

def initialize():
    parser = argparse.ArgumentParser(usage='%(prog)s [-h] (--train | --predict | --eval) (--regression | --classification)'
                                                    '[--trainx TRAINX] [--trainy TRAINY] [--devx DEVX] [--devy DEVY]'
                                                    '[--model MODEL] [--preds PREDS] [--lr LR] [--max-steps MAX_STEPS]'
                                                    '[--mb MB] [--patience PATIENCE] [--dev_freq DEV_FREQ] [--verbose]'
                                                    '[--L L] [--activation {relu,tanh,sigmoid}] [--C C]',)                       
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--train", action="store_true", help="Train a DNN model from X and Y.")
    mode.add_argument("--predict", action="store_true", help="Run prediction on a dev/test set using a trained model.")
    mode.add_argument("--eval", action="store_true", help="Evaluate a trained model on a dev/test set.")
    task = parser.add_mutually_exclusive_group(required=True)
    task.add_argument("--regression", action="store_true", help="Use identity output activation with squared error loss.")
    task.add_argument("--classification", action="store_true", help="Use softmax output activation with cross-entropy loss.")

    parser.add_argument('--trainx', default='', help="Path to training inputs .npy.")
    parser.add_argument('--trainy', default='', help="Path to training targets .npy (y values or class labels).")
    parser.add_argument('--devx', default='', help="Path to dev/test inputs .npy.")
    parser.add_argument('--devy', default='', help="Path to dev/test targets .npy (y values or class labels).")
    parser.add_argument("--model", default='model.npz', help="Path to model file to write/read, default \"model.npz\".")
    parser.add_argument("--preds", help="Path to write predictions .npy (used with --predict).")
    parser.add_argument("--lr", type=float, help="Learning rate for gradient descent/MB-SGD.")
    parser.add_argument("--max-steps", type=int, default=5000, help="Max MB-SGD steps, default 5000.")
    parser.add_argument('--mb', type=int, default=32, help="Mini-batch size, default 32.")
    parser.add_argument('--patience', type=int, default=10, help="Early stopping patience (number of dev evals without improvement), default 10.")
    parser.add_argument('--dev_freq', type=int, default=500, help="Evaluate on the dev set every this many gradient steps, default 500.")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose mode, in which each minibatch loss is printed.")
    parser.add_argument('--L', default="32x1", help='Number of hidden layers and sizes: a comma delimited list of nunits by nlayers specifiers [default: "32x1"]'
                                                'Examples: "32x3", "32x2,64x2", "128x30", "128x2,16x1,128x2".'
                                                'Use an empty string ("") for a linear model (no hidden layers).')
    parser.add_argument('--activation', choices=['relu', 'tanh', 'sigmoid'], default='relu', help="Hidden layer activation, default \"relu\".")
    parser.add_argument('--C', type=int, help="Number of classes (classification) or output dimension (regression).")


    args = parser.parse_args()
    if args.train and not (args.trainx and args.trainy and args.devx and args.devy and args.lr and args.C):
        parser.error("--train requires the following arguments: --trainx --trainy --devx --devy --lr --C")
    elif args.predict and not (args.devx and args.preds):
        parser.error("--predict requires the following arguments: --devx --preds")
    elif args.eval and not (args.devx and args.devy):
        parser.error("--eval requires the following arguments: --devx --devy")

    return args






#===================================================================================
#Training mode:
# Training Set:
#   Inputs: N_tr x D matrix
#   Targets: N_tr vector
# N_tr = number of training examples
# D = number of features 
# Target vector shape and type depends on task
# Regression: N_tr x C matrix, C is output dimension of each target
# Classification: N_tr vector of class labels from 0 to C-1
# Trains using mini-batch stochastic gradient descent with model checkpointing and early stopping
# Model weights initialized with Glorot initilization, biases initialized to 0
#===================================================================================
def train_model(trainx, trainy, devx, devy, model, lr, max_steps, mb, patience, dev_freq, verbose, L, activation, C):
    N, D = np.shape(trainx)
    layers = L.split(",")
    #Setup weight and bias matrices
    W = []
    b = []
    #Each item in L is of the form "unitsxlayers"
    for i in range(len(layers)):
        units, layers = layers[i].split("x")
    
    
  

    # Check for inconsistency in provided arguments
    


    steps, lossChange = 0
    epoch = 1
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

#Glorot Initilization
# Weights = uniform distribution of 
#        /      6         \         /      6         \
# -sqrt  | -------------  | , sqrt  | -------------  |
#        \ L_{l-1}+{L_l}) /         \ L_{l-1}+{L_l}) /
#
# L_{l-1} is dimension of previous layer
# L_{l} is dimension of layer l
# Input is N x D where D is dimension

#===================================================================================
#Prediction mode:
# Takes a trained model, and new set of input
# makes predictions for each input, storing result to a file
# - N x D nd array of type np.float64
# - N is the number of data points
# - D is the dimensionality of each input vector
#===================================================================================
def model_predictions(devx, model):
    N, D = np.shape(devx)
    weights = []
    biases = []
    layers = len(model['layer_sizes'])
    activation = model['activation']

    for i in range(1, layers+1):
        weights.append(model[f"W_{i}"])
        biases.append(model[f"b_{i}"])
    
    for i in range(layers):
        w = weights[i]
        b = biases[i]
        if np.shape(w)[0] != D:
            sys.exit(f"Input dimension {D} does not match model weight dimension {np.shape(w)[0]} for layer {i+1}")
        D = np.shape(w)[1]
        if np.shape(b)[0] != D:
            sys.exit(f"Bias dimension {np.shape(b)[0]} does not match weight output dimension {D} for layer {i+1}")
        devx = np.dot(devx, w) + b
        if i != layers -1:
            devx = activate(devx, activation)

    if model['task'] == 'classification':
        devx = softmax(devx)
    
    return devx

def activate(x, activation):
    if activation == 'relu':
        return np.maximum(0, x)
    elif activation == 'tanh':
        return np.tanh(x)
    elif activation == 'sigmoid':
        return 1 / (1 + np.exp(-x))

def softmax(z):
    expZ = np.exp(z - np.max(z, axis=1, keepdims=True)) 
    return (expZ / np.sum(expZ, axis=1, keepdims=True))

#===================================================================================
#Evaluation mode:
# Takes a trained model, and an N x D matrix and vector of N targets
# Targets are integers from 0 to C-1 or vectors of length C
#===================================================================================
def model_eval(devx, devy, model):
    N, D = np.shape(devx)
    if N != np.shape(devy)[0]:
        sys.exit(f"Dev inputs {N} and outputs {np.shape(devy)[0]} are not the same length")
    p = model_predictions(devx, model)
    if model['task'] == 'classification':
        return accuracy(p, devy)
    elif model['task'] == 'regression':
        mean = np.mean(devy, axis=0)
        return 1-(np.sum(np.square(devy-p))/np.sum(np.square(devy-mean)))
    
def accuracy(p, devy):
    classes = np.argmax(p, axis=1)
    correct = np.sum(classes == devy)
    return correct / np.shape(devy)[0]

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
        evaluation = model_eval(devx, devy, model)
        print(f"{evaluation:.3f}")


if __name__ == "__main__":
    main()