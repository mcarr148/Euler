import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath
#Prime factorize 20 to 1, adding in factors that aren't in our dict - multiply at the end

limit = 20
factor_dict = {}
for num in range(20,0,-1):
    cur_factors = MyMath.prime_factorize(num)
    for prime,power in cur_factors.items():
        if factor_dict.get(prime,0) < power:
            factor_dict[prime] = power

print(math.prod(k**v for k,v in factor_dict.items()))