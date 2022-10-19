class Solution:

    def check(self, N, M, Edges): 
        adj = [[] for i in range(N+1)]
        for edge in Edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = [False]*(N+1)
        
        def exist_path( adj, i, count, N, visited):
        
            if visited[i]:
                return False
            if count == N:
                return True
            visited[i] = True
            for node in adj[i]:
                if exist_path(adj, node, count+1, N, visited):
                    return True
            visited[i] = False
            return False
        
        for i in range(1, N+1):
            if exist_path(adj, i, 1, N, visited):
                return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends