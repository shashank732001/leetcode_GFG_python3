class Solution:
	def isEularCircuitExist(self, V, adj):
		#Code here
        """
         Euler circuit = all no nodes should have only even edges
         Euler path = n-2 nodes should have even edges and other two should have odd
         """
		
		count = 0
		for i in range(V):
		    if len(adj[i])%2!=0:
		        count+=1
       
		if count==0:
		    return 2

		return 1 if count==2 else 0    


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEularCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends