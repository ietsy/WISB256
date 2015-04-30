import sys
import time

T1 = time.perf_counter()

try:
    maxnumber = int(sys.argv[1])
    output = open(sys.argv[2], 'w')

except:
    print("Please give the input in the following style:")
    print("pythonfile maximum-number outputfile")

def findprimes(maxnr ):
    # for maxnr < 3 it's faster to just give the primes. The loop and checks take more time
    if maxnr < 2: return [] # if the max is two there are no primes
    if maxnr < 3: return [2] # if the max is three the only prime is 2
    prim = []
    multiples = set()
    for i in range(2, maxnr+1):
        if i not in multiples:
            prim.append(i)
            multiples.update(range(i*i, maxnr+1, i))
    return prim

primlist = findprimes(maxnumber)
for i in range(len(primlist)):
    output.write(str(primlist[i]) + '\n')

nrprimes = str(len(primlist))

T2 = time.perf_counter()
print('Found ', nrprimes, ' Prime numbers smaller than ', maxnumber, ' in ', T2 - T1)