#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        
        l = 0
        # maximum distance possible is last ele, so our distance has to be lesser than this
        # if we have more than one cow
        r = stalls[-1]
        ans = 0
        while l<=r:
            mid = (l+r)//2
            #considering half the distance to increase cow count
            
            cow = 1
            prev = stalls[0]
            for i in range(1,n):
                if stalls[i]-prev>=mid:
                    cow+=1
                    prev = stalls[i]
            
            if cow>=k:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends