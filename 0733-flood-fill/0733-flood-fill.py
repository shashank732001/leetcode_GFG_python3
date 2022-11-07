class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([(sr,sc)])
        rows = len(image)
        cols = len(image[0])
        source_color = image[sr][sc]
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        visited.add((sr,sc))
        image[sr][sc]=color
        
        while q:
            r,c = q.popleft()
            
            for dr,dc in directions:
                row = r+dr
                col = c+dc
                
                if row not in range(rows) or col not in range(cols) or image[row][col]!=source_color or (row,col) in visited:
                    continue
                    
                visited.add((row,col))
                image[row][col] = color
                q.append((row,col))
        return image        
            
        