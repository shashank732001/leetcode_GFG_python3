class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def subs(arr,out,res):
            
            if len(arr)==0:
                res.append(out)
                return
            
            out1 = out[:]
            out2 = out[:]
            out2.append(arr[0])
            subs(arr[1:],out1,res)
            subs(arr[1:],out2,res)
            return
        
        res = []
        out = []
        subs(nums,out,res)
        return res
            
            