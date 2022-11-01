#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        left = N
        i = 0
        j = N-1
        Min = 0
        Max = 0
        
        while left>0:
            Min+=candies[i]
            Max+=candies[j]
            left=left-K-1
            i+=1
            j-=1
        return Min, Max    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends