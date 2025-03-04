import math

def sievePrimesToN(n):
    if n < 2: return -1

    potential_primes = [i for i in range(0,n+1)]
    potential_primes[1] = 0
    for num in range(2,n+1):
        if num == 0: continue
        multiple = 2
        while (num*multiple <= n):
            potential_primes[multiple*num]=0
            multiple+=1

    return [i for i in potential_primes if i >0]

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

test =genPermutations([1,2,3,9],"num")
#print(len(test))
#print(test)
#print(set(test))