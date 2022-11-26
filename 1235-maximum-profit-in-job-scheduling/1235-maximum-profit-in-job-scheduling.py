class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime,endTime,profit))
        jobs.sort(key=lambda i : i[0])  #sort based on start time
        dp = [-1]*(n+1)
        
        # @lru_cache(None)
        
        def helper(i):
            
            if i==n:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            j = i+1
            
            while j<n and jobs[i][1]>jobs[j][0]:
                j+=1
            
            one = jobs[i][2]+helper(j)
            two = helper(i+1)
            
            dp[i]=max(one,two)
            return dp[i]
        
        return helper(0)