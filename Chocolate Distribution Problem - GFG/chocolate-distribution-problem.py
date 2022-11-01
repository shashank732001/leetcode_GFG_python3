#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        i = 0
        j = i+(M-1)
        ans  = max(A)
        
        while j<N:
            min_pack = A[i]
            max_pack = A[j]
            
            ans = min(ans,max_pack-min_pack)
            i+=1
            j+=1
        return ans    
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends