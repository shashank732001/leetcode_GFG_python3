#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        missing  = sum(range(n+1))-sum(set(arr))
        repeating = None
        hashmap= {}
        for i in arr:
            hashmap[i]=1+hashmap.get(i,0)
            if hashmap[i]>1:
                repeating = i
                break
        return repeating,missing
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends