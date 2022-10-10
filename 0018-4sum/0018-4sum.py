class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums =sorted(nums)
        n =len(nums)
        res =[]
        for i in range(n-3):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                temp_sum = target-(nums[i]+nums[j])
                l = j+1

                r = n-1
                while l < r :
                    
                    if (nums[l]+nums[r]==temp_sum):
                        a=[nums[i],nums[j],nums[l],nums[r]]
                        
                        res.append(a)
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<temp_sum:
                        l+=1
                    else:
                        r-=1
                
        return res   