#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        celeb = [0]*n
        
        for i in range(n):
            for j in range(n):
                if M[i][j] ==1:   # this means i knows j
                # so we increase j's popularity 
                # since celebrity knows noone i's popularity will be decremented by 1
                    celeb[j]+=1
                    celeb[i]-=1
                    
        for key, val in enumerate(celeb):
            if val == (n-1):
                return key
        return -1            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends