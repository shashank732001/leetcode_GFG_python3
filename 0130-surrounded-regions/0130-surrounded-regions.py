class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        # finding "O" at the borders   ["O"--->"T"]
        def dfs(r,c):
            
            if (r not in range(rows) or 
                c not in range(cols) or 
                board[r][c]!="O"):
                return
            
            board[r][c]="T"
            
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in (0,rows-1) or c in (0,cols-1)):
                    dfs(r,c)
        
        # Now capturing all the "O"    ["O"--->"X"]
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                    
        # Now unmarking all the "T"    ["T"--->"O"]  
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
                    