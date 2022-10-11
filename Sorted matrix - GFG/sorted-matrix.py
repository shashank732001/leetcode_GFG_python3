#User function Template for python3
import numpy as np
class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        mat = sorted(np.array(Mat).flatten())
        # print(mat)
        res = [[0]*N for i in range(N)]
        k = 0
        
        for i in range(N):
            for j in range(N):
                res[i][j]= mat[k]
                k+=1
                
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends