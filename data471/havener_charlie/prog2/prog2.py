import numpy as np
import argparse

#Create a program that trains and evaluates
#liner regression models.

# x is input, a vector with D dimensions
# w is vector of weights, with D dimensions
# b is the scalar bias term
# y is the scalar model output

#Will focus on D=C=1 and D>1, C=1

#Will also support polynomial fitting
#===================================================================================
#Training mode:
# Takes training set of an N_trD matrix of
#inputs and a vector of N_tr outputs
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
#===================================================================================
#Prediction mode:
# Program takes a trained model, and new set of input
# makes predictions for each input, storing result to a file
# - one line per datapoint
# - each line is a single number in scientific notation, with 3 decimal points
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

if __name__ == "__main__":
    # usage: prog2.py [-h] (--train | --predict | --eval) [--order ORDER] [--x X] [--y Y][--model MODEL] [--preds PREDS] [--lr LR] [--max-steps MAX STEPS]
    parser=argparse.ArgumentParser()
    parser.add_argument("--train", help="Train a model from x.txt and y.txt.")
    parser.add_argument("--predict", help="Run prediction on a dev set using a trained model.")
    parser.add_argument("--eval", help="Evaluate a trained model on a dev set (prints MSE).")
    parser.add_argument("--order")
    parser.add_argument("--x")
    parser.add_argument("--y")
    parser.add_argument("--model")
    parser.add_argument("--preds")
    parser.add_argument("--lr")
    parser.add_argument("--max-steps")
    parser.parse_args()
