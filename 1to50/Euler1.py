import sys
import os

sys.path.append(os.path.abspath(".."))
import MyMath 

limit = 999
    
print(MyMath.sumMultsToL(3,limit)+MyMath.sumMultsToL(5,limit)-MyMath.sumMultsToL(15,limit))