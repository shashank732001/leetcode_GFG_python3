class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        visited = [False]*n
        Sum = sum(nums)
        if Sum%k!=0:return False
        nums.sort(reverse=True)
        reqSum = Sum//k
        subSets = [0]*k
        
        def recurse(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= nums[i]

                    # Important line, otherwise function will give TLE
                    if subSets[j] == 0:
                        break
                        
            return False
        
        return recurse(0) 
                    

    
    