class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        
        def backtrack(curr,pos,target):
            
            if target == 0:
                res.append(curr)
                
            if target <= 0:
                return
            
            prev = -1
            
            for i in range(pos,len(candidates)):
                
                if candidates[i]==prev:
                    continue
                    
                curr1 = curr[:]
                curr1.append(candidates[i])
                backtrack(curr1,i+1,target-candidates[i])
                
                prev = candidates[i]
                
        res = []
        backtrack([],0,target)
        return res
                