import numpy as np
import argparse
from pathlib import Path
#Create a program that trains and evaluates
#liner regression models.

# x is input, a vector with D dimensions
# w is vector of weights, with D dimensions
# b is the scalar bias term
# y is the scalar model output

#Will focus on D=C=1 and D>1, C=1

#Will also support polynomial fitting



def initialize():
    parser = argparse.ArgumentParser(usage='%(prog)s [-h] (--train | --predict | --eval) [--order ORDER] [--x X] [--y Y]'
                                                        '[--model MODEL] [--preds PREDS] [--lr LR] [--max-steps MAX_STEPS]')                       
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--train", action="store_true", help="Train a model from x.txt and y.txt.")
    mode.add_argument("--predict", action="store_true", help="Run prediction on a dev set using a trained model.")
    mode.add_argument("--eval", action="store_true", help="Evaluate a trained model on a dev set (prints MSE).")

    parser.add_argument('--order', type=int, default=1, help="Polynomial order (1 for linear model, default 1).")
    parser.add_argument('--x', default='', help="Path to inputs x.txt.")
    parser.add_argument("--y", default='', help="Path to targets y.txt.")
    parser.add_argument("--model", default='', help="Path to model file to be written.")
    parser.add_argument("--preds", default='', help="Path to write predictions (predict).")
    parser.add_argument("--lr", help="Learning rate for gradient descent.")
    parser.add_argument("--max-steps", type=int, default=0, help="Max gradient steps; 0 means analytical solution (train), default 0.")
    return parser.parse_args()


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
def train_model(order, inputs, targets, model, lr, steps):
    return


#===================================================================================
#Prediction mode:
# Program takes a trained model, and new set of input
# makes predictions for each input, storing result to a file
# - one line per datapoint
# - each line is a single number in scientific notation, with 3 decimal points
#===================================================================================
def model_predictions(order, inputs, model, lr, predictions):
    m = open(model).readline.split()
    b = m[0]
    w = np.fromstring(m[1:])
    print(b)
    print(w)
    return

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
    return

def main():
    path = Path(__file__).resolve().parent
    args = initialize()
    order = args.order
    inputs = path / args.x
    targets = path / args.y
    model = path / args.model
    predictions = path / args.preds
    lr = args.lr
    steps = args.max_steps

    if args.train:
        train_model()
    elif args.predict:
        model_predictions(order, inputs, model, lr, predictions)
    elif args.eval:
        model_eval(order, inputs, targets, model)

if __name__ == "__main__":
    main()