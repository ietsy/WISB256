import sys
import time

T1 = time.perf_counter()

maxnumber = int(sys.argv[1])
output = open(sys.argv[2], 'w')

primlist = [2, 3, 5, 7]

for i in range(len(primlist)):
    output.write(str(primlist[i]) + '\n')


T2 = time.perf_counter()

print('Time required', T2 - T1, 'sec.')
