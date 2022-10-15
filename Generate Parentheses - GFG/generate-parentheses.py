#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        def generate(openn,close,out,res):
            
            if openn==0 and close==0:
                res.append(out)
                return
            
            if openn>0:
                out1 = out
                out1=out1+"("
                generate(openn-1,close,out1,res)
                
            if close>openn:
                out2 = out
                out2 = out2+")"
                generate(openn,close-1,out2,res)
            return    
        
        openn = n
        close = n
        out = ""
        res = []
        generate(openn,close,out,res)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends