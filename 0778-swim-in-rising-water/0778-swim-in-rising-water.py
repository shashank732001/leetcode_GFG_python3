class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minheap = [[grid[0][0],0,0]] #[time/max-height , r,c] to sort based on time
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        visit.add((0,0))
        
        while minheap:
            time,r,c = heapq.heappop(minheap)
            
            if r==n-1 and c==n-1:
                return time
            
            for dr,dc in directions:
                row = r+dr
                col = c+dc
                
                if row not in range(n) or col not in range(n) or (row,col) in visit:
                    continue
                    
                visit.add((row,col))
                heapq.heappush(minheap,[max(time,grid[row][col]),row,col])