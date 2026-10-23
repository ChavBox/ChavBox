import numpy as np
import argparse
import sys
from pathlib import Path

def initialize():
    parser = argparse.ArgumentParser(usage='%(prog)s [-h] (--train | --predict | --eval) [--order ORDER] [--x X] [--y Y]'
                                                        '[--model MODEL] [--preds PREDS] [--lr LR] [--max-steps MAX_STEPS]')                       
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--train", action="store_true", help="Train a model from x.txt and y.txt.")
    mode.add_argument("--predict", action="store_true", help="Run prediction on a dev set using a trained model.")
    mode.add_argument("--eval", action="store_true", help="Evaluate a trained model on a dev set (prints MSE).")

    parser.add_argument('--order', type=int, default=1, help="Polynomial order (1 for linear model, default 1).")
    parser.add_argument('--x', default='', help="Path to inputs x.txt.")
    parser.add_argument("--y", help="Path to targets y.txt.")
    parser.add_argument("--model", default='', help="Path to model file to be written.")
    parser.add_argument("--preds", help="Path to write predictions (predict).")
    parser.add_argument("--lr", help="Learning rate for gradient descent.")
    parser.add_argument("--max-steps", type=int, default=0, help="Max gradient steps; 0 means analytical solution (train), default 0.")

    args = parser.parse_args()
    if args.train and not (args.x and args.y and args.model):
        parser.error("--train requires the following arguments: --x --y --model")
    elif(args.max_steps>0 and not args.lr):
        parser.error("--train requires --lr when --max-steps > 0")
    elif args.predict and not (args.x and args.model and args.preds):
        parser.error("--predict requires the following arguments: --x --model --preds")
    elif args.eval and not (args.x and args.y and args.model):
        parser.error("--eval requires the following arguments: --x --y --model")
    return args

#===================================================================================
#Training mode:
# Takes training set of an N_trD matrix of
# inputs and a vector of N_tr outputs
#N_tr: number of training examples
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
def train_model(order, inputs, targets, model_path, lr, steps):
    if steps == 0:
        model = train_analytical(order, inputs, targets)
    else:
        model = train_gd(order, inputs, targets, float(lr), steps)
    np.savetxt(model_path, model, fmt="%.3e", newline=" ")
    return

def train_analytical(order, inputs, targets):
    ones = np.ones(np.shape(inputs)[0])
    features = np.column_stack((ones, inputs))
    inverse = np.dot(np.transpose(features), features)
    try:
        inverse = np.linalg.inv(inverse)
    except np.linalg.LinAlgError:
        sys.exit("Matrix is unable to be inverted")
    
    return np.dot(np.dot(np.transpose(features), targets), inverse)


def train_gd(order, inputs, targets, lr, steps):
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
# - one line per datapoint
# - each line is a single number in scientific notation, with 3 decimal points
#===================================================================================
def model_predictions(order, inputs, model):
    b = model[0]
    w = model[1:]
    return np.dot(inputs, w)+b

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
def model_eval(order, inputs, targets, model):
    p = model_predictions(order, inputs, model)
    error = np.mean(np.square(targets-p))
    print(f"{error:.3e}")

def main():
    args = initialize()
    inputs = np.loadtxt(args.x, ndmin=2)
    if args.y:
        targets = np.loadtxt(args.y, ndmin=1)
        if targets.shape[0] != inputs.shape[0]:
            print("x and y must have the same number of rows")
            return
    if args.max_steps < 0:
        print("max-steps must be >= 0")
        return


    if args.train:
        train_model(args.order, inputs, targets, args.model, args.lr, args.max_steps)
    elif args.predict:
        p = model_predictions(args.order, inputs, np.loadtxt(args.model))
        np.savetxt(args.preds, p, fmt='%.3e')
    elif args.eval:
        model_eval(args.order, inputs, targets, np.loadtxt(args.model))

if __name__ == "__main__":
    main()