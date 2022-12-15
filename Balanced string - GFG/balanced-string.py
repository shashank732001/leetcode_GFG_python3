#User function Template for python3

class Solution:
    def BalancedString(self,N):
        #code here
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        old_N = N
        res = ''
        while N>26:
            res+=alpha
            N = N-26
        
        if N%2==0:
            cut = N//2
            res+=alpha[:cut]+alpha[26-cut:]
        
        elif N%2!=0:
            Sum = sum(int(i) for i in str(old_N))
            if Sum%2==0:
                cut1 = (N+1)//2
                cut2 = (N-1)//2
                res+=alpha[:cut1]+alpha[26-cut2:]
            else:
                cut1 = (N-1)//2
                cut2 = (N+1)//2
                res+=alpha[:cut1]+alpha[26-cut2:]
        return res        
                
                
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends