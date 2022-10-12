#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        # res = [-1]*n
        # stack =[0]
        # for i in range(1,n):
        #     while stack and arr[i]>arr[stack[-1]]:
        #         res[stack.pop()] =arr[i]
        #     stack.append(i)
        # return res    
        
        
        res = []
        
        stack = []
        
        for i in range(n-1,-1,-1):
            if not stack:
                res.append(-1)
            
            elif stack and stack[-1]>arr[i]:
                res.append(stack[-1])
                
            else:
                while stack and stack[-1]<=arr[i]:
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
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends