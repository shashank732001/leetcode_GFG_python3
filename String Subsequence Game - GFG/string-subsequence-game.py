#User function Template for python3
class Solution:
    def allPossibleSubsequences (ob, S):
        # code here 
        vowels = "aeiou"
        
        def subs(arr,out,res):
            
            if len(out)>=2:
                if out[0] in vowels and out[-1] not in vowels:
                    res.append(out)
            
            if len(arr)==0:
                return
            
            
            subs(arr[1:],out,res)
            subs(arr[1:],out+arr[0],res)
            return
        
        res = []
        out = ""
        subs(S,out,res)
        

        res = list(set(res))
        return sorted(res)
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        ans=set()
        ob = Solution()
        ans = ob.allPossibleSubsequences(S)
        if(len(ans)==0):
            print(-1, end = "")
        else:
            for i in ans:
                print(i,end=" ")
        print()
# } Driver Code Ends