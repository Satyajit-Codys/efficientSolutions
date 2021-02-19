n = int(input())


def primeNumber(n):
    if n == 1: return False
    #We can save many cases by putting extra checks like if 'N%2==0' and 'N%3==0'
    if n==2 or n==3: return True
    if(n%2==0 or n%3==0): return False
    for i in range(3,int(n**0.5)): #0 to square root of N
        if n%i==0 or n%(i+2)==0:
            return False
        i +=6
    return True
    
print(primeNumber(n))