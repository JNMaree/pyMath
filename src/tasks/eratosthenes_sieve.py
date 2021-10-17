import numpy

def setupSieve(max):
    if max%2 == 0:
        elements = max
    else:
        elements = max + 1
    
    primePotential = numpy.zeros((int(elements/2), 2), dtype=numpy.uint32)
    primePotential[0,0] = 2
    primePotential[0,1] = 1

    j = 1
    
    for i in range(3, elements, 2):
        primePotential[j,0] = i
        primePotential[j,1] = 1
        j+=1

    return primePotential
    
def runSieve(arrPrimePotentials):
    max = arrPrimePotentials[-1, 0]
    for i in range(1, int(numpy.sqrt(max))):
        j = 3
        if arrPrimePotentials[i, 1] == 1:
            mul = arrPrimePotentials[i,0]
            loopy = True
            while loopy:
                mul = arrPrimePotentials[i,0]*j
                j += 2
                if mul <= max:
                    arrPrimePotentials[int(mul/2),1] = 0
                else:
                    loopy = False
            
def printPrimes(sieve):
    out = ""
    prime_count = 0
    for i in range(0, sieve.shape[0]):
        if sieve[i,1] == 1:
            out += str(sieve[i,0]) + ", "
            prime_count += 1
    print(out)

def main():
    
    #test
    max = 101
    primes = setupSieve(max)
    runSieve(primes)
    printPrimes(primes)
    
if __name__ == "__main__":
    main()