# Generate primes
# Author: Darren Miller

primes= []
upto= 1001
for candidate in range(2, upto):
    #print (candidate)
    isPrime= True
    #only need to check if divisable by prime
    for divisor in primes:
        if (candidate % divisor ==0):
            isPrime= False
            break
    if isPrime:
        primes.append(candidate)

print (primes)

