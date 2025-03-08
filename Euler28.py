import sys
import os
import math
sys.path.append(os.path.abspath(".."))
import MyMath

#Somewhat ugly solution but we're going to just increase the jumps every 4 steps

limit = 1001*1001
diag_sum = 1
next_pos = 3
step_size = 2
steps_taken = 0


while(next_pos <= limit):
    #print(next_pos)
    diag_sum += next_pos
    steps_taken +=1
    if steps_taken == 4:
        steps_taken = 0
        step_size+=2
    next_pos += step_size

print(diag_sum)