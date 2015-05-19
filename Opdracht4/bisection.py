import sys
import math

def findRoot(f, a, b, epsilon):
    # Calculate the midpoint
    m = (a + b) / 2
    # Terminate if the endpiont is the root
    if f(m) == 0:
        return m
    # Check if the half is larger than epsilon else return midpoint
    elif math.fabs(m-a) <= epsilon:
        return m
    # See what half we need to check next
    if f(m) * f(a) < 0:
        return findRoot(f, a, m, epsilon)
    if f(m) * f(b) < 0:
        return findRoot(f, m, b, epsilon)