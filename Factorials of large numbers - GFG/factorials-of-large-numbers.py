#User function Template for python3

class Solution:
    def factorial(self, N):
        #code here
        # dp = [1]*(N+1)
        # dp[0] = 1
        # for i in range(1,N+1):
        #     dp[i]=dp[i-1]*i
        # return [dp[-1]]
        
        # arr = []
        # count = 1
        # for i in range(1,N+1):
        #     arr.append(i)
        
        # for i in range(len(arr)):
        #     count*=arr[i]
        # return [count]    
        
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)    
        
        ans = fact(N)
        return [ans]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends