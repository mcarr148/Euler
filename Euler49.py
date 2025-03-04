import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath
#Find 4 digit primes, then just print out the ones with 3+ permutations in candidates to scope out the problem space
limit = 10000

p_options = [i for i in MyMath.sievePrimesToN(limit) if i > 1000]
prime_set = set(p_options)

print(p_options)

p_intersection = []
for prime in p_options:
    perms = MyMath.genPermutations(str(prime),"num")
    if len(prime_intersection :=  set(perms).intersection(prime_set)) > 3:
       # print(prime_intersection)
        p_intersection.append(sorted(list(prime_intersection)))

jump_primes = []
for p_perms in p_intersection:
    print(p_perms)
    for prime in p_perms:
        if (prime+3330) in p_perms and (prime+3330*2) in p_perms and p_perms not in jump_primes:
            jump_primes.append(p_perms)
            continue
print(jump_primes)