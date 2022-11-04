#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        # char_stack = []
        # index_stack = []
        # index_stack.append(-1)
        # Len = 0
        
        # for i in range(len(S)):
            
        #     if S[i]=="(":
        #         char_stack.append(S[i])
        #         index_stack.append(i)
                
        #     else:
        #         if char_stack:
        #             char_stack.pop()
        #             index_stack.pop()
        #             Len = max(Len,i-index_stack[-1])
        #         else:
        #             index_stack.append(i)
        # return Len            
        
        
        
        # index_stack = []
        # index_stack.append(-1)
        # Len = 0
        
        # for i in range(len(S)):
            
        #     if S[i]=="(":
        #         index_stack.append(i)
                
        #     else:

        #         index_stack.pop()
        #         if not index_stack:
        #             index_stack.append(i)
                    
        #         else:
        #             Len = max(Len,i-index_stack[-1])
        # return Len 
                    
                    
        n = len(S)            
        opened = 0
        closed = 0
        Len = 0
        
        #substring from the start
        
        for i in range(n):
            if S[i]=="(":
                opened+=1
            else:
                closed+=1
            
            if opened == closed :
                Len = max(Len,opened+closed)
            elif closed>opened:
                opened = 0
                closed = 0
                
        opened = 0
        closed = 0

        #substring from the end
        
        for i in range(n-1,-1,-1):
            if S[i]=="(":
                opened+=1
            else:
                closed+=1
            
            if opened == closed :
                Len = max(Len,opened+closed)
            elif opened>closed:
                opened = 0
                closed = 0        
        
                
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