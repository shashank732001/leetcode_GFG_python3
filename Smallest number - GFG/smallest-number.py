#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        # code here 
        
        if 9*D<S:
            return "-1"
    
        
        ans = ""
        Sum = S-1
        i=0
        
        while i<(D-1):
            
            if Sum>9:
                ans = "9"+ans
                Sum-=9
                
            else:
                ans  = str(Sum)+ans
                Sum-=Sum
                
            i+=1
        
        ans = str(Sum+1)+ans    
        return ans
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends