#User function Template for python3

def downwardDigonal(N, A): 
#     # code here 
    # rows = len(A)
    # cols = len(A[0])
    # visited = set()
    # res = []
    
    
    # def helper(row,col,res):
        
    #     if row not in range(rows) or col not in range(cols) or (row,col) in visited:
    #         return
        
        
    #     res.append(A[row][col])
    #     visited.add((row,col))
    #     helper(row+1,col-1,res)
    #     return
    
    # for i in range(rows):
    #     for j in range(i,cols):
    #         helper(i,j,res)
    # return res  

        arr = []
        for i in range(N):
            for j in range(i+1):
                arr.append(A[j][i-j])
        for i in range(N-1):
            for j in range(1+i,N):
                arr.append(A[j][i-j])
        return arr
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends