import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath
'''Find the longest collatz seq generating number under 1 million
 divide by 2 if n is even 
 multiply by 3 and add 1 if n is odd'''
limit = 10**6

def nextCollatz(n):

    if n < 2: return -1
    if n%2 == 0: return n//2
    return n*3 + 1

#Store lengths we've found
collatzLens = {1:1}

def calcCollatzLen(n):
#    print(n)
    if n < 1: return 0
    if n == 1: return 1
    if n in collatzLens: return collatzLens[n]
    seq_len = 1
    next_col = nextCollatz(n)
    seq_len += calcCollatzLen(next_col)
    collatzLens[n] = seq_len
    return seq_len

for i in range(1,limit):
    calcCollatzLen(i)

best = max(collatzLens,key=collatzLens.get)
print(best)
print(collatzLens[best])
'''for key,value in collatzLens.items():
    print(f'num {key}   | len {value}')'''
