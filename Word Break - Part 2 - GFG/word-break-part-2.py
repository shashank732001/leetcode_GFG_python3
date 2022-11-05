#User function Template for python3

class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        ans=[]
        d = dict
        m=len(s)
        flag=[[False for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if(s[i:j+1] in d):
                    flag[i][j]=True
        def solve(start,ans,temp,m):
            if(start>=m):
                ans.append(' '.join(temp.copy()))
                return
            for i in range(m):
                if(flag[start][i]==True):
                    temp.append(''.join(s[start:i+1]))
                    solve(i+1,ans,temp,m)
                    temp.pop()
            return
        temp=[]
        solve(0,ans,temp,m)
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