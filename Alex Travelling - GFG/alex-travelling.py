#User function Template for python3
from collections import deque
from typing import List
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        # code here
        adj = {}
        dist = [0]*(n+1)
        
        for u,v,w in flights:
            adj[u] = adj.get(u,[])+[[v,w]]
        
        # print(adj[2])
        q = deque([])    
        q.append([k,0])
        
        while q:
            node,cost = q.popleft()
            if node not in adj:
                continue
            for nei in adj[node]:
                nei_node = nei[0]
                nei_cost = nei[1]
                if (dist[nei_node]==0 or dist[nei_node]>cost+nei_cost) and nei_node!=k:
                    dist[nei_node]=cost+nei_cost
                    q.append([nei_node,dist[nei_node]])
        
        ans = 0
        for i in range(1, n+1):
            
            if dist[i]!=0:
                ans = max(ans,dist[i])
            
            elif dist[i]==0 and i!=k:
                return -1
        return ans        
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends