
def naiveMethod(n):
    result = []
    for i in range(2,n):
        if primeNumber(i)==True:
            result.append(i)
    return result


def primeNumber(n):
    if n == 1: return False
    #We can save many cases by putting extra checks like if 'N%2==0' and 'N%3==0'
    if n==2 or n==3: return True
    if(n%2==0 or n%3==0): return False
    for i in range(5,int(n**0.5)): #0 to square root of N
        if n%i==0 or n%(i+2)==0:
            return False
        i +=6
    return True


# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def SieveOfEratosthenes(n): 
	
	# Create a boolean array "prime[0..n]" and initialize 
	# all entries it as true. A value in prime[i] will 
	# finally be false if i is Not a prime, else true. 
	prime = [True for i in range(n + 1)] 
	p = 2
	while (p * p <= n): 
		
		# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			
			# Update all multiples of p 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers 
	for p in range(n + 1): 
		if prime[p]: 
			print(p)

# driver program 
if __name__=='__main__': 
	n = int(input())
	print("Following are the prime numbers smaller")
	print("than or equal to", n) 
	SieveOfEratosthenes(n) 
