class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        rows, cols = len(matrix), len(matrix[0])
        # visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        if rows <= 1 and cols <= 1:
            return 1
    
        def dfs(i, j):
            if dp[i][j] != -1: return dp[i][j]
            dp[i][j] = 1
            
            
            for dr,dc in directions:
                row = i+dr
                col = j+dc
                if row in range(rows) and col in range(cols) and matrix[row][col]>matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(row, col))
            
            return dp[i][j]
        
        ans  = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        
        return ans
        