class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = int((n*(n+1))/2-sum(set(nums)))
        duplicate = sum(nums)-sum(set(nums))
        # lookup = {}
        # for i in nums:
        #     lookup[i]=lookup.get(i,0)+1
        # duplicate = [i for i in nums if lookup[i]==2] 
        return [duplicate,missing]
        