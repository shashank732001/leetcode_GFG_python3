#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        
        sundays = S//7
        buy_days = S-sundays
        total_food = S*M
        days = (S*M)//N
        
        if (S*M)%N!=0:
            days+=1
        
        if days<=buy_days:
            return days
        return -1    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends