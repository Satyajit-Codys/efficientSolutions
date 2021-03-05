n = int(input())

#Using String Reverse (slicing)
def palindrome(n):
    string = str(n)
    return (string == string[::-1])
       
answer = palindrome(n)
print(answer)


#Mathematical Approach
def palindrome_num(n):
    reverse = 0
    temp = n
    while(temp > 0):
        reverse = reverse * 10 + (temp%10)
        temp = temp//10
    return(n == reverse)

print(palindrome_num(n))
