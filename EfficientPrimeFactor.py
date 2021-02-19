n = int(input())

def primeFactor(n):
    if n <= 1: return 
    for i in range(2,int(n**0.5)):
        while(n%i==0):
            print(i)
            n = n//i
    if n>1:
        print(n)

primeFactor(n)