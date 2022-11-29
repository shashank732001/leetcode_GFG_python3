class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numdict = {
            
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
            
            
        }
        out = []
        if digits == '':return out
#         for i in digits:
#             temp=[]
#             for j in dict[i]:
                
#                 for k in out:
#                     temp.append(k+j)
#             out = temp
#         return out  
        def backtrack(i,curr):
            if len(curr)==len(digits):
                out.append(curr)
                return
            
            for c in numdict[digits[i]]:
                backtrack(i+1,curr+c)
        
        backtrack(0,"")
        return out
        
                    
            