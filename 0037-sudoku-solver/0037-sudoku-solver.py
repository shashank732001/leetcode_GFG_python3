class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         def valid(num,i,j,board,n):
            
#             #checking along the row
#             for k in range(n):
#                 # print(i,k)
#                 if board[i][k]==num:
#                     return False
                
#             #checking along the col    
#             for k in range(n):
#                 # print(k,j)
#                 if board[k][j]:
#                     return False
            
#             # checking the submatrix
            
#             s = sqrt(n)
#             start_row = i-i%s
#             start_col = j-j%s
            
#             for row in range(start_row,start_row+s):
#                 for col in range(start_col,start_col+s):
#                     if board[row][col]==num:
#                         return False
#             return True        
        
        def isvalid(row,col,board,num):
            c=str(num)
            for i in range(9):
                if board[i][col]==c: return False
                if board[row][i]==c: return False
                if board[3*(row//3)+ i//3][3*(col//3) + i%3]==c: return False
                
            return True
    
    
        n = len(board)    
            
        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    for num in range(1,n+1):
                            
                        if isvalid(i,j,board,num):
                            board[i][j]=str(num)
                                
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True  
        
        
#         def isvalid(row,col,board,c):
#             c=str(c)
#             for i in range(9):
#                 if board[i][col]==c: return False
#                 if board[row][i]==c: return False
#                 if board[3*(row//3)+ i//3][3*(col//3) + i%3]==c: return False
                
#             return True
        
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]==".":
#                     for c in range(1,10):
#                         if isvalid(i,j,board,c):
#                             board[i][j]=str(c)                         
#                             if self.solveSudoku(board):
#                                 return True
#                             else:
#                                 board[i][j]="."
#                     return False
#         return True
                    
            
        
            