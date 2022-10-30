class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        q=deque([(0,0,k,0)])
        seen=set()
        directions =[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y,left,steps=q.popleft()
            if (x,y,left) in seen or left<0:
                continue
            if (x,y)==(rows-1,cols-1):
                return steps
            seen.add((x,y,left))
            
            if grid[x][y]==1:
                left-=1
                
            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if new_x in range(rows) and new_y in range(cols):
                    q.append((new_x,new_y,left,steps+1))
                    
        return -1
        