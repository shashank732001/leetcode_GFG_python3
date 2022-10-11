
from collections import deque
class Solution:
    

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		q = deque()
		fresh,time = 0,0    # to keep track of time and fresh oranges
		rows = len(grid)
		cols = len(grid[0])
		
		for r in range(rows):
		    for c in range(cols):
		        if grid[r][c]==1:
		            
		            fresh+=1             # we get the number of fresh oranges present
		        if grid[r][c]==2:
		            q.append([r,c])      # we get the position of rotten oranges
		
		directions = [[0,1],[0,-1],[1,0],[-1,0]]      # neighbouring positions
		
		while q and fresh>0:
		    
		    for i in range(len(q)):
		        r,c = q.popleft()              # getting the position of rotten oranges from top
		        for dr,dc in directions:
		            row,col = dr+r,dc+c         # adding neigh condn
		            
		            if (row<0 or row == len(grid)
		            or col <0 or col==len(grid[0])    # checking if the position is out of bounds or the orange at position is not fresh one
		            or grid [row][col]!=1):     #skipping the condition
		                continue
		            
		            grid[row][col]=2     # if fresh one we make it rotten 
		            q.append([row,col])        # and add its position to our q
		            fresh-=1                    # fresh number decreases
		             
		            
		    time+=1                   # each rotting cycle
		    
		return time if fresh==0 else -1    
		            
		





"""
we cannot use dfs for this problem coz dfs means we will move for one rotten orange till its end then we move to other so time becomes more 

but the condition given to us is each oranges which are rotten simultaneously rot the neighbouring ones so we can use multi source bfs 
with queue having each initial rotten oranges

sice we are visiting the pos only once the 
time--> O(n.m)
space -->O(n.m) coz of q and recursion
"""
#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends