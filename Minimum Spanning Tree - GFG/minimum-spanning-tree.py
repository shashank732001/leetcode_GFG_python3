#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        parent = [-1]*V
        keys = [float("inf")]*V
        keys[0]=0
        mst = [False]*V
        
        
        for count in range(V-1):
            
            Min = 10e9
            ind = -1
            
            for e in range(V):
                if not mst[e] and keys[e]<Min:
                    Min = keys[e]
                    ind = e
            mst[ind] = True     
            
            for child in adj[ind]:
                v = child[0]
                weight = child[1]
                
                if not mst[v] and weight<keys[v]:
                    parent[v] = u
                    keys[v] = weight
        return sum(keys)            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends