class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        mirror_map = {i:[] for i in A}
        
        for i in range(0,2*e,2):
            mirror_map[A[i]].append(A[i+1])
            
        
        for i in range(0,2*e,2):
            if B[i+1]!=mirror_map[B[i]][-1]:
                return 0
            mirror_map[B[i]].pop()    
        return 1        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.checkMirrorTree(n,e,A,B))
# } Driver Code Ends