class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Djikstra's Algo"""
        
        edges = collections.defaultdict(list)
        
        for u,v,w in times:
            edges[u].append([v,w])
            
        res = 0
        visit = set()
        minheap = [[0,k]] #cost, node (to sort based on cost/time)
        
        while minheap:
            time,node = heapq.heappop(minheap)
            if node in visit:
                continue
                
            visit.add(node)
            res = max(res,time)
            
            for nei,neiTime in edges[node]:
                if nei not in visit:
                    heapq.heappush(minheap,[time+neiTime,nei])
        return res if len(visit)==n else -1           