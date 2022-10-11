class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row  = len(grid)
        col  =len(grid[0])
        
        res = [[10e9]*(col+1) for i in range(row+1)]
        res[row-1][col] = 0
        
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                res[i][j]=grid[i][j]+min(res[i+1][j],res[i][j+1])
        return res[0][0]        