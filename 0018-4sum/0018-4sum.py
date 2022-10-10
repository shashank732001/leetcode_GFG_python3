class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums =sorted(nums)
        n =len(nums)
        res =[]
        for i in range(n-3):
            for j in range(i+1,n-2):
                
                l = j+1

                r = n-1
                while l < r :
                    fsum = nums[i]+nums[j]+nums[l]+nums[r]
                    if fsum == target:
                        a=[nums[i],nums[j],nums[l],nums[r]]
                        if a not in res:
                            res.append(a)
                        l+=1
                    elif fsum<target:
                        l+=1
                    else:
                        r-=1
                
        return res   