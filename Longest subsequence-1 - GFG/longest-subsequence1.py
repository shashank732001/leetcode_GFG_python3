#User function Template for python3

class Solution:
    def longestSubsequence(self, N, A):
        # code here
        if N==1:return 1
        
        dp = [1]*(N)
        for i in range(N-1,-1,-1):
            for j in range(i+1,N):
                if abs(A[i]-A[j])==1:
                    dp[i]=max(dp[i],1+dp[j])
    
        return max(dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))
# } Driver Code Ends