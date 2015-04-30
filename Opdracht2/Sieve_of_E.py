import sys
import time



# import the give files
try:
    maxnumber = int(sys.argv[1])
    output = open(sys.argv[2], 'w')

except:
    print("Please give the input in the following style:")
    print("pythonfile maximum-number outputfile")
    quit()


#do the Sieve
def findprimes(maxnr ):
    # for maxnr < 3 it's faster to just give the primes. The loop and checks take more time
    if maxnr < 2: return [] # if the max is two there are no primes
    if maxnr < 3: return [2] # if the max is three the only prime is 2

    # making a list to skip al multiples
    multiples = set() # a list with all multiples included. Gets filled in the loop
    multiples.update(range(2*2, maxnr+1, 2)) # Remove all even numbers
    prim = [2] # because we skip all even numbers, the rest of the script skips 2. So we add it here

    # below the Sieve
    for i in range(3, maxnr+1, 2): # stepsize 2 because we can skip all even numbers
        if i not in multiples:
            prim.append(i)
            multiples.update(range(i*i, maxnr+1, i))
    
    # return the list of primes
    return prim


# write the list of primes to the output file
T1 = time.perf_counter()
primlist = findprimes(maxnumber)
T2 = time.perf_counter()

output.write(str(primlist[0]))
for i in range(1, len(primlist)):
    output.write('\n')
    output.write(str(primlist[i]))
output.close()

# print the output
print('Found ', str(len(primlist)), ' Prime numbers smaller than ', maxnumber, ' in ', T2 - T1)