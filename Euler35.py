import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath


#Generate a list of primes. Then compute the FAIL*permuations*FAIL of each, add them to circular primes if they are a subset.
#add 2 to base set and check for 2,4,6,8 in number to cut down on candidates
#Circular just means digit rotations :) read the definitions carefully
limit = 999999
primes = MyMath.sievePrimesToN(limit)
circ_primes ={2}
prime_set = set(primes)

def genDigitRotations(num):
    rotations = [num]
    for i in range(len(str(num))-1):
        num = (num%10)*(10**(len(str(num))-1))+num//10
        rotations.append(num)
    return rotations

for prime in primes:
    if prime in circ_primes:
        continue
    if any(d in "2468" for d in str(prime)):
        continue
    candidates = genDigitRotations(prime)
    if(set(candidates).issubset(prime_set)):
        circ_primes.update(candidates)

#print(primes)
circ_primes = list(set(circ_primes))
circ_primes.sort()

