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


T2 = time.perf_counter()

print('Time required', T2 - T1, 'sec.')
