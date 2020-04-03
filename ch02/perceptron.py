import numpy as np

# two-input perceptron.
# x is an array of 2 in length.
# w is weight(an array of 2 in length), b is bias(integer).
def perceptron2(x, w, b):
    if b + np.sum(x * w) <= 0:
        return 0
    else:
        return 1

def AND2(x):
    w, b = np.array([1, 1]), -1.5
    return perceptron2(x, w, b)

def NAND2(x):
    w, b = np.array([-1, -1]), 1.5
    return perceptron2(x, w, b)
    
def OR2(x):
    w, b = np.array([1, 1]), -0.5
    return perceptron2(x, w, b)

def XOR2(x):
    x1 = NAND2(x)
    x2 = OR2(x)
    s = np.array([x1, x2])
    return AND2(s)

for x in [np.array(x) for x in [[0,0], [0,1], [1,0], [1,1]]]:
    print(x, "->", AND2(x), NAND2(x), OR2(x), XOR2(x))