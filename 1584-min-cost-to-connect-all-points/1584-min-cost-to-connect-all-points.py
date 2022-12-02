class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)} # holds a list of [cost,node] here cost is dist
        
        #creating a adjacency list
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                #since our graph is undirected we need to add to both
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        
        
        """Prim's Algo"""
        res = 0
        visit = set()
        minheap = [[0,0]]  #[cost,node] to sort based  on min cost
        
        while len(visit)<n:
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,[neiCost,nei])

        return res