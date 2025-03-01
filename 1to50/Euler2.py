import sys
import os

sys.path.append(os.path.abspath(".."))
import MyMath 

limit = 4000000
print(sum([i for i in MyMath.fibsToN(limit) if i%2 ==0]))