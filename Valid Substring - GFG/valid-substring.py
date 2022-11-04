#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        char_stack = []
        index_stack = []
        index_stack.append(-1)
        Len = 0
        
        for i in range(len(S)):
            
            if S[i]=="(":
                char_stack.append(S[i])
                index_stack.append(i)
                
            else:
                if char_stack:
                    char_stack.pop()
                    index_stack.pop()
                    Len = max(Len,i-index_stack[-1])
                else:
                    index_stack.append(i)
        return Len            
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends