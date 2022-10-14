#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        
        def search(s,k):
            if k ==1:
                s.pop()
                return
            val = s[-1]
            s.pop()
            search(s,k-1)
            s.append(val) 
            return
        
        n = sizeOfStack
        if n == 0:
            return s
            
        k = (n//2)+1
        search(s,k)
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends