class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row_set = set()
        col_set = set()
        
        for i in range(rows):
            row_set.clear()
            col_set.clear()
            for j in range(cols):
                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])
            
            if len(row_set)!=rows or len(col_set)!=cols:
                return False

        return True
                
                
        