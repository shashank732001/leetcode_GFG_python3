#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a.sort()
        Sum = 0
        mod = (10**9)+7
        for i in range(n):
            Sum+=(i*a[i])
        return Sum%mod   
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends