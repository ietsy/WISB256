import sys
import math

def findRoot(f, a, b, epsilon):
    print("a= ", a, f(a))
    print("b= ", b, f(b))
    # Calculate the midpoint
    m = (a + b) / 2
    print("m= ", m, f(m))
    # Terminate if the endpiont is the root
    if f(m) == 0:
        return m
    # Check if the half is larger than epsilon else return midpoint
    elif math.fabs(m-a) <= epsilon:
        return m
    
    # See what half we need to check next
    if f(m) * f(a) < 0:
        print("tussen a en m")
        return findRoot(f, a, m, epsilon)
    if f(m) * f(b) < 0:
        print("tussen m eb b")
        return findRoot(f, m, b, epsilon)
    print("There was an error, this can be:")
    print("The conditions must be: a < b and either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0")
    print("try different values for a and b")