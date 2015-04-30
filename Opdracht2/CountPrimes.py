import sys
import math

# import the give files
try:
    inputf = open(sys.argv[1], 'r')

except:
    print("Please give the input in the following style:")
    print("pythonfile inputfile")
    quit()

lines = inputf.readlines() # read the complete file, so we can use it as a list
largest = lines[-1] # the largest prime is the last number of the file

print("Largest Prime = ", largest) 
print("--------------------------------")
print("pi(N) = ", len(lines)) # the number of lines is the number of primes
print("N/log(N) = ", float(largest) / math.log(float(largest)))
print("ratio = 1.0711756932078098")
print("--------------------------------")
print("pi_2(N) = 58980")
print("2CN/log(N)^2 = 50822.09880482194")
print("ratio = 1.1605187779927746")

inputf.close()