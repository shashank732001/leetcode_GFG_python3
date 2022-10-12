#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here

        
        if N==1:return Matrix[0][0]
        
        for i in range(N-2,-1,-1):
            for j in range(N):
                if j==0:
                    Matrix[i][j]+=max(0,Matrix[i+1][j],Matrix[i+1][j+1])
                
                elif j==N-1:
                    Matrix[i][j]+=max(0,Matrix[i+1][j],Matrix[i+1][j-1])
                    
                else:
                    Matrix[i][j]+=max(Matrix[i+1][j-1],Matrix[i+1][j],Matrix[i+1][j+1])
                    
        # print(Matrix)       
        return max(i for i in Matrix[0])        
        
        
        
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends