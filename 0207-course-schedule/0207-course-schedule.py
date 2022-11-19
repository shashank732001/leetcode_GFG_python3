class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         preMap = {i:[] for i in range(numCourses)}  
        
#         for cour , pre in prerequisites:
#             preMap[cour].append(pre)
            
#         visitSet = set()
        
#         def dfs(cour):
#             if cour in visitSet:
#                 return False
            
#             if preMap[cour]==[]:
#                 return True
            
#             visitSet.add(cour)
#             for pre in preMap[cour]:
#                 if not dfs(pre):return False
#             visitSet.remove(cour)
#             preMap[cour] = []
#             return True
        
#         for crs in range(numCourses):
#             if not dfs(crs):return False
#         return True 

        N = numCourses
    
        indeg = [0]*N
        adj = [[] for i in range(N)]
        for (src, dest) in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1
        
        q = deque([]) 
        for node in range(N):
            if indeg[node]==0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        for i in range(N):
            if indeg[i] != 0:
                return False
        return True