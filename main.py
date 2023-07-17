from math import sqrt
def findRows(x):
    n=(sqrt(8*x+1)-1)//2
    return int(n)
x=int(input("n= "))
print(findRows(x))