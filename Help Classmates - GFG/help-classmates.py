#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack = []
        res = []
        for i in range(n-1,-1,-1):
            if not stack:
                res.append(-1)
                
            elif stack and stack[-1]<arr[i]:
                res.append(stack[-1])
                
            else:
                while stack and stack[-1]>=arr[i]:
                    stack.pop()
                if stack:
                    res.append(stack[-1])
                else:
                    res.append(-1)
            stack.append(arr[i])
        return res[::-1]    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends