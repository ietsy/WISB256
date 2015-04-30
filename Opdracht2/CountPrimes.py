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
devide = float(largest) / math.log(float(largest))

def findpi_2():
    count = 0
    for i in range(2, len(lines)):
        if int(lines[i]) - int(lines[i-1]) == 2:
            count = count + 1
    return count

pi_2 = findpi_2()
C2 = 0.6601618
devide2 = 2*C2*float(largest)/math.log(float(largest))**2

print("Largest Prime = ", largest) 
print("--------------------------------")
print("pi(N) = ", len(lines)) # the number of lines is the number of primes
print("N/log(N) = ", devide)
print("ratio = ", len(lines) / devide)
print("--------------------------------")
print("pi_2(N) = ", pi_2)
print("2CN/log(N)^2 = ", devide2)
print("ratio = ", pi_2 / devide2)

inputf.close()