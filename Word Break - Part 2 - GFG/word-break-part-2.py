#User function Template for python3

class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        ans=[]
        d = dict
        
        def func(i,st):
            if i==len(s):
                ans.append(st[:-1])
                return
            for j in range(i,len(s)+1):
                if s[i:j] in d:
                    func(j,st+s[i:j]+' ')
        func(0,'')
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends