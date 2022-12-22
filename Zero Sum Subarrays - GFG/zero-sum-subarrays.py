#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        count = 0
        lookup = {}
        curr_sum = 0
        
        for i in arr:
            curr_sum+=i
            
            if curr_sum==0:
                count+=1
            
            count+=lookup.get(curr_sum,0)
            
            lookup[curr_sum] = 1+lookup.get(curr_sum,0)
            
        return count    
            
        
        #return: count of sub-arrays having their sum equal to 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends