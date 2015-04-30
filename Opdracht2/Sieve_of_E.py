import sys
import time

# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
T1 = time.perf_counter()

maxnumber = int(sys.argv[1])
output = open(sys.argv[2], 'w')

for i in range(maxnumber):
    output.write(str(i) + '\n' )

T2 = time.perf_counter()

print('Time required', T2 - T1, 'sec.')
