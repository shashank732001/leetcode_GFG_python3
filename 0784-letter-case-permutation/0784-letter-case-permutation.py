class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def perm(inp,out,res):
            
            if len(inp)==0:
                if out not in res:
                    res.append(out)
                return
            
            out1 = out
            out2 = out
            if not inp[0].isnumeric():
                out1 = out1+inp[0].upper()
                out2 = out2+inp[0].lower()
            else:
                out1 = out1+inp[0]
                out2 = out2+inp[0]
            
            perm(inp[1:],out1,res)
            perm(inp[1:],out2,res)
            return
        
        res = []
        out = ""
        perm(s,out,res)
        return res