class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        zeros = 0
        output = [0]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    zeros += 1
                if grid[i][j]==1:
                    start = (i,j)

        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or (i, j) in visited or grid[i][j]==-1:
                return
            visited.add((i, j))
            if grid[i][j] == 2 and zeros + 2 == len(visited):
                output[0] += 1
                visited.remove((i, j))
                return

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            visited.remove((i,j))
            
        i,j = start
        visited = set()
        dfs(i,j)
        return output[0]