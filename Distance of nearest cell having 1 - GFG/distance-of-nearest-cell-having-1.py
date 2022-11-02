
from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		
		q = deque([])
		rows = len(grid)
		cols = len(grid[0])
		distance = [["."]*cols for i in range(rows)]
		visited = set()
		directions = [[1,0],[-1,0],[0,1],[0,-1]]
		
		for i in range(rows):
		    for j in range(cols):
		        if grid[i][j]==1:
		            visited.add((i,j))
		            q.append(((i,j),0))
		            distance[i][j]=0
		
		while q:
		    (r,c),step = q.popleft()
		    
		    for dr,dc in directions:
		        row = r+dr
		        col = c+dc
		        
		        if row not in range(rows) or col not in range(cols) or (row,col) in visited or grid[row][col]==1:
		            continue
		        
		        
		        distance[row][col] = step+1
		        visited.add((row,col))
		        q.append(((row,col),step+1))
		return distance        
		        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends