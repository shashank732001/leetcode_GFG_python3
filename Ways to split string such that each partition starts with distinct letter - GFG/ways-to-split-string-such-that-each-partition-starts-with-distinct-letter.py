#User function Template for python3

class Solution:
    def waysToSplit(self, S):
        # code here
        lookup = {}
        for i in S:
            lookup[i]=1+lookup.get(i,0)
        lookup[S[0]]=1
        res = 1
        for i in lookup.keys():
            
            res*=lookup[i]
        return res%1000000007        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.waysToSplit(S))
# } Driver Code Ends