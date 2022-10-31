#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        def factorial(mid,n):
            
            prod = 5
            c = 0
            
            while prod<=mid:
                
                c+=(mid//prod)
                prod *=5
            
            return c>=n
            
        if n==1:
            return 5
            
        low = 0
        high = 5*n
        
        while low<high:
            
            mid = (low+high)//2
            
            if factorial(mid,n):
                high = mid
                
            else:
                low = mid+1
        return low        
            
                
              


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends