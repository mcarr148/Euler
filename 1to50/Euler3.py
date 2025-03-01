import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath
'''Finding the largest prime factor of a number. Initial thought
is to find all the primes to sqrt(n) and brute force test from there'''
limit = 600851475143
root = math.floor(limit**(.5))
potential_primes = MyMath.SievePrimesToN(root)

max = -1
for prime in potential_primes:
    if limit % prime == 0:
        max = prime
print(max)


