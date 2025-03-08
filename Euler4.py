#1 liner just because
print(max([i*j for i in range(100,1000) for j in range(100,1000) if str(j*i) == str(j*i)[::-1]]))