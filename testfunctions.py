from functions import multiplytwonumbers as ms
from functions import multiplypower as power
print(ms(6,7))
print(power(6,7,8))
a=[]
for i in range(0,21,2):
    a.append(ms(i , i+1))
print(a)