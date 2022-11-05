#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        zeros = 0
        ones = 0
        count = 0
        n = len(str)
        if n%2!=0:
            return -1
        
        for i in str:
            if i =="0":
                zeros+=1
            else:
                ones+=1
            if zeros==ones:
                count+=1
                ones = 0
                zeros = 0
        return count if ones==zeros else -1       




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends