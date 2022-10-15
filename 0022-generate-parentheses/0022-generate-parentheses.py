class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(openn,close,out,res):
            
            if openn==0 and close==0:
                res.append(out)
                return
            
            if openn>0:
                out1 = out
                out1 = out1+"("
                generate(openn-1,close,out1,res)
                
            if close>openn:
                out2 = out
                out2 = out2+")"
                generate(openn,close-1,out2,res)
                
            return    
        
        openn = n
        close = n
        out = ""
        res= []
        generate(openn,close,out,res)
        return res
        
#         out = []
        
#         def rec(l,r,st,br):
#             if l == r == 0:
#                 out.append(br)
#                 return 
#             if l>0:
#                 rec(l-1,r,st+1,br+"(")
#             if r>0 and st>0:
#                 rec(l,r-1,st-1,br+")")
#         rec(n,n,0,"") 
#         return out

        