#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    stack = []
    ans = ""
    for i in S:
        stack.append(i)
    while stack:
        char = stack.pop()
        ans+=char
    return ans    
        
        
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends