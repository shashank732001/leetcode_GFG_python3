#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        """
        brute approach time--> O(n**2)
        """
        # parent = [-1]*V
        # keys = [float("inf")]*V
        # keys[0]=0
        # mst = [False]*V
        
        
        # for count in range(V-1):
            
        #     Min = 10e9
        #     ind = -1
            
        #     for e in range(V):
        #         if not mst[e] and keys[e]<Min:
        #             Min = keys[e]
        #             ind = e
        #     mst[ind] = True     
            
        #     for child in adj[ind]:
        #         v = child[0]
        #         weight = child[1]
                
        #         if not mst[v] and weight<keys[v]:
        #             parent[v] = u
        #             keys[v] = weight
                    
        # return sum(keys)            
        
        
        """
        little optimization using heap
        """
        # parent = [-1]*V
        # keys = [float("inf")]*V
        # keys[0]=0
        # mst = [False]*V
        # pq = []
        # heapq.heappush(pq,[0,0])
        
        
        # while pq:
            
        #     # Min = 10e9
        #     top = heapq.heappop(pq)
        #     ind = top[1]
        #     mst[ind]=True

        #     for child in adj[ind]:
        #         v = child[0]
        #         weight = child[1]
                
        #         if not mst[v] and weight<keys[v]:
        #             parent[v] = u
        #             keys[v] = weight
        #             heapq.heappush(pq,[keys[v],v])
                    
        # return sum(keys)   
        
        """
        kruskal algo
        
        """
        
        
        def findparent(element,ds):
            if element==ds[element]:
                return element
            ds[element] = findparent(ds[element],ds)
            return ds[element]
        
        ds = []
        for i in range(V):
            ds.append(i)
        rank = [1]*V
        pq = []
        
        for i in range(V):
            
            v = adj[i]
            
            for child in v:
                heapq.heappush(pq,[child[1],[i,child[0]]])
        
        count = 0
        Sum = 0
        
        while count<(V-1):
            
            top = heapq.heappop(pq)
            dist = top[0]
            ele1 = top[1][0]
            ele2 = top[1][1]
            p1 = findparent(ele1,ds)
            p2 = findparent(ele2,ds)
            
            if p1!=p2:
                
                if rank[p1]<rank[p2]:
                    ds[p1]=p2
            
                elif rank[p1]>rank[p2]:
                    ds[p2]=p1
                else:
                    ds[p1]=p2
                    rank[p2]+=1
                
                count+=1
                Sum+=dist
            
        return Sum
        
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