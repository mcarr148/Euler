import sys
import os
import math
import MyMath

#Changing the limit to **7 and pretending I remembered to check the digit sum of 8/9 to be mults of 3 :)
limit = 10**7

primes = MyMath.sievePrimesToN(limit)
max_pan = -1

def isPandigital(n):
    digits = [int(d) for d in str(n)]
    #print(digits)
    return (max(digits) <= len(digits)) and (0 not in digits) and (len(set(digits)) == len(digits))

for prime in primes:
    if isPandigital(prime):
        max_pan = prime

print(max_pan)