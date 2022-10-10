#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        lookup = {}
        res =[]
        for i in arr:
            lookup[i]=lookup.get(i,0)+1
        
            
        res = [val for key,val in lookup.items()]
        res.sort()
        # print(lookup)
        # print(res)
        return [key for key,val in lookup.items() if val==res[-2]][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends