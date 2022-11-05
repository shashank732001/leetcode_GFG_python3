#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        
        n = len(S)
        res = []
        
        def subs(start,out):
            
            
            if start==n:
                res.append(out)
                return
            
            for i in range(start,n):
                if S[start:i+1]==S[start:i+1][::-1]:
                    subs(i+1,out+[S[start:i+1]])
        

        subs(0,[])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends