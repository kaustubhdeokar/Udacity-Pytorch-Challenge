import numpy as np
import math
# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    total=0
    for i in range(len(Y)):
        total+=Y[i]*(-math.log(P[i]))+(1-Y[i])*(-math.log(1-P[i]))
    return total
