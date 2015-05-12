import sys
import math
import random

def drop_needle(L):
    x0 = random.random()
    theta = random.vonmisesvariate(0,0)
    xe = x0 + L * math.cos(theta)

    if xe < 0:
        return True
    elif xe > 1:
        return True
    return False

def smallL(N, L):
    count = 0
    for i in range(N):
        if drop_needle(L):
            count = count + 1
        
    pi_estimate = 2 * L / (count / N)

    print(count, " hits in ", N, " tries")
    print("Pi = ", pi_estimate)
    sys.exit()

def bigL(N, L):
    count = 0
    for i in range(N):
        if drop_needle(L):
            count = count + 1

    pi_estimate = 2 * (1 - math.sqrt(L**2 -1) - math.asin( (1 / L) )) / ( (count / N) - 1)

    print(count, " hits in ", N, " tries")
    print("Pi = ", pi_estimate)
    sys.exit()

try:
    Ngiven = int(sys.argv[1])
    Lgiven = float(sys.argv[2])
    if len(sys.argv) == 4:
        random.seed(int(sys.argv[3]))
except:
    print("Use: estimate_pi.py N L (seed)")
    sys.exit()

if Lgiven <= 1:
    smallL(Ngiven, Lgiven)
else:
    bigL(Ngiven, Lgiven)