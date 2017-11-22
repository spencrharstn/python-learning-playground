# Generate prime numbers

import math
import time

primes1 = []
primes2 = []

# Version 1

def find_primes(upper_limit):
    count = 0 #number of primes found
    candidate = 1 #the current integer to be tested if prime
    while(candidate <= upper_limit): # loop until the upper limit is reached
        divisor = 2 #the divisor for the candidate
        is_prime = 1 #boolean if candidate is prime
        while(divisor**2 <= candidate and is_prime):
            if(candidate % divisor == 0):
                is_prime = 0
            divisor += 1
        if(is_prime):
            primes1.append(candidate)
            count += 1
        candidate += 2
    return count

# Version 2. Much faster. From: http://www.geeksforgeeks.org/sieve-of-eratosthenes/
def find_primes2(limit):
    primes_array = [True for i in range(limit + 1)] #create a limit list of Trues
    count = 0 #number of primes found
    p = 2 #the first prime

    while(p * p <= limit):
        if(primes_array[p] == True):
            for i in range(p * 2, limit + 1, p):
                primes_array[i] = False
        p += 1

    for p in range(2, limit): #count up to the limit, starting at 2
        if(primes_array[p]): #if the current item at index p is True, then index p is a prime number
            primes2.append(p) #add to list of primes
            count += 1 #count number of primes found

    return count

limit = int(input('What is the upper limit?: '))

t0 = time.perf_counter()
count1 = find_primes(limit)
t1 = time.perf_counter()

t2 = time.perf_counter()
count2 = find_primes2(limit)
t3 = time.perf_counter()

print(primes1)
print(primes2)
print(" Ver1: Found %d primes in %s seconds" %(count1,t1 - t0))
print(" Ver2: Found %d primes in %s seconds" %(count2,t3 - t2))
