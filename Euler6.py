#Diff between sum of squares and suare of sum

limit = 100

def square_of_sum(n):
    return (n*(n+1)/2)**2

def sum_of_squares(n):
    return (n*(2*n+1)*(n+1))/6

print(square_of_sum(limit)-sum_of_squares(limit))