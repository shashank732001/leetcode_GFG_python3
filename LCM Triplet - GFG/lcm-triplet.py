#User function Template for python3

class Solution:
    def lcmTriplets(self,N):
        #code here
        #base case
        if N<=2:
            return N
        
        #odd case
        if N%2!=0:
            return N*(N-1)*(N-2)
        
        # if number is divided by 6 .,  lets consider 6 5 4  here 6 and 4 have coomon terms and 6 and 3 have coomon terms so consider  5 4 3
        if N%6==0:
            return (N-1)*(N-2)*(N-3)
        
        return (N)*(N-1)*(N-3)    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob=Solution()
        print(ob.lcmTriplets(N))
# } Driver Code Ends