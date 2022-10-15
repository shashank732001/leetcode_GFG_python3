#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        def perm(inp,out,res):
            
            if len(inp)==0:
                res.append(out)
                return
            
            out1 = out
            out2 = out
            out1 = out1+" "+inp[0]
            out2 = out2+inp[0]
            perm(inp[1:],out1,res)
            perm(inp[1:],out2,res)
            return
            
        out = S[0]
        res= []
        perm(S[1:],out,res)
        return sorted(res)




#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends