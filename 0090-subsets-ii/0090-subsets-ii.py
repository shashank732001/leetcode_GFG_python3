class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def subs(inp,out,res):
            
            if len(inp)==0:
                if out not in res:
                    res.append(out)
                return
            
            out1 = out[:]
            out2 = out[:]
            out2.append(inp[0])
            subs(inp[1:],out1,res)
            subs(inp[1:],out2,res)
            return
        
        nums.sort()
        out = []
        res = []
        subs(nums,out,res)
        return res