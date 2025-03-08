import math
import numpy as np

def sievePrimesToN(n):
    if n < 2: return -1

    potential_primes = np.ones(n+1, dtype = bool)
    potential_primes[0:2] = False

    for num in range(2,int(n**.5)+1):
        if potential_primes[num]:
            potential_primes[num*num:n+1:num] = False

    return np.flatnonzero(potential_primes).tolist()

#print(len(sievePrimesToN(10**9)))

def sumMultsToL(n, L):
    #break multiples into pairs, multiply by the number of pairs
    if n < 0: return -1
    n_mults = math.floor(L/n)

    pair_sum = n + n*n_mults
    num_pairs = n_mults / 2

    return round(pair_sum * num_pairs)

def fibsToN(n):
    if n< 1: return -1
    if n == 1: return [1]
    fibs = [1,2]
    fib_next = 3
    while (fib_next <= n):
        fibs.append(fib_next)
        fib_next = fibs[-1] + fibs[-2]

    return fibs

def genPermutations(input_list, list_type):
    #Take the members of a group and arrange them in all possible combinations
    if not input_list: return []
    if len(input_list) ==1:
        if list_type== "num":
            return [int(input_list[0])]
        return input_list[0]
    perms = []
    if list_type == "num":
        a_list = [str(i) for i in input_list]
    else:
        a_list = input_list.copy()

    for item in a_list:
        l_copy = a_list.copy()
        l_copy.remove(item)
        for outcome in genPermutations(l_copy,list_type):
            perms.append(str(item)+str(outcome))
    if list_type == "num":
        perms = [int(i) for i in perms]

    return perms

primes_for_factorizing =[0]

def prime_factorize(n):
    #Trial division
    if n == 0:
        return 0
    global primes_for_factorizing
    if max(primes_for_factorizing) < math.ceil(n**.5):
        primes_for_factorizing = sievePrimesToN(math.ceil(n**.5))
    p_factors = {}
    pos = 0
    #print(primes_for_factorizing, len(primes_for_factorizing))
    while(True):
        #print(n)
        #print(pos)
        if n%primes_for_factorizing[pos] == 0:
            p_factors[primes_for_factorizing[pos]] = 1 + p_factors.get(primes_for_factorizing[pos],0)
            n = n//primes_for_factorizing[pos]
        else:
            pos+=1
        if n == 1 or pos == len(primes_for_factorizing):
            if len(primes_for_factorizing) == pos:
                p_factors[n] = 1
            break
    #print(p_factors)
    return p_factors

#print(prime_factorize(123400))


test =genPermutations([1,2,3,9],"num")
#print(len(test))
#print(test)
#print(set(test))