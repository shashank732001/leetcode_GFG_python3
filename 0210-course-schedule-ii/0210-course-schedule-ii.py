class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}  
        ans  = []
        for cour , pre in prerequisites:
            preMap[cour].append(pre)
            
        visitSet = set()
        
        def dfs(cour):
            if cour in visitSet:
                return False
            
            if preMap[cour]==[]:
                if cour not in ans:
                    ans.append(cour)
                return True
            
            visitSet.add(cour)
            for pre in preMap[cour]:
                if not dfs(pre):return False
                
            visitSet.remove(cour)
            preMap[cour] = []
            if cour not in ans:
                ans.append(cour)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):return []
        return ans 