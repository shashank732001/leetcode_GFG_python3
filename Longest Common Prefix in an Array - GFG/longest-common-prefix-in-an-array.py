#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        min_word = min(arr)
        ptr = 0
        res =""
        for i in range(len(min_word)):
            for j in range(n):
                if min_word[ptr]!=arr[j][ptr]:
                    if len(res) == 0:
                        return -1
                    else:return res
            res+=min_word[ptr]
            ptr+=1
        return res    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends