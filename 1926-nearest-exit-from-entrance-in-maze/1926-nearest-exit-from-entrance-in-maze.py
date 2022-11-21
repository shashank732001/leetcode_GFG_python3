from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])
        
        exits = set()
        
        for i in range(rows):
            for j in range(cols):
                if ((i==0 or i==rows-1 or j==0 or j==cols-1)
                and [i,j]!=entrance and maze[i][j]!="+"):
                        exits.add((i,j))
        
        if len(exits)==0:
            return -1
        
        q = deque([])
        visited = set()
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        q.append((entrance,0))
        visited.add(tuple(entrance))
        
        
        while q:
            
            [r,c],steps  = q.popleft()
            
            if (r,c) in exits:
                return steps
            
            for dr,dc in directions:
                row = dr+r
                col = dc+c
                
                if (row in range(rows) and col in range(cols) 
                   and maze[row][col]!="+" and (row,col) not in visited):
                    
                    
                    q.append(([row,col],steps+1))
                    visited.add((row,col))
        return -1        