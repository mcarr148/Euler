import sys
import os
import math
import MyMath
from fractions import Fraction

'''Iterate through a double loop, check if the digits match.
'''
start = 10
end = 99

def share_digit(num1,num2):
    if any(d in str(num1) for d in str(num2)):
        matching = []
        if str(num1//10) in str(num2):
            matching.append(num1//10)
        if str(num1%10) in str(num2):
            matching.append(num1%10)
        return matching
    return False

def is_digit_cancel(digit, num, denom):
    new_num = 0
    new_denom = 0
    if num//10 == digit:
        num = num%10
    else: new_num = \
        new_num = num//10

    if denom//10 == digit:
        new_denom = denom%10
    else: new_denom = \
        new_denom = denom//10
    print(num,denom,digit)
    print(new_num,new_denom)
    return abs(new_num/new_denom - num/denom) < .001
cancel_fracs = []

for denom in range(start,end):
    for num in range(start,denom):
        if digits := (share_digit(num,denom)):
            for digit in digits:
                if ('0' not in str(num) and '0' not in str(denom) and num%11 != 0):
                    if(is_digit_cancel(digit, num, denom)):
                        cancel_fracs.append([num,denom])

cancel_num = 1
cancel_denom = 1
for circ in cancel_fracs:
    cancel_num  *= circ[0]
    cancel_denom *= circ[1]

print(Fraction(cancel_num,cancel_denom))