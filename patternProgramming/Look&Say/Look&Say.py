
class Solution:

    def lookandsay(self, n):
        if n==1: return "1"
        if n==2: return "11"
        string = "11"
        for i in range(3,n+1):
            string +='$'
            length = len(string)
            
            count = 1
            temp = ""
            
            for j in range(1,length):
                if string[j]!=string[j-1]:
                    temp += str(count)
                    temp += string[j-1]
                    count = 1
                else: count += 1
            string = temp
        return string
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends
