class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        first =nums[0]
        second =10e9
        
        for i in range(1,n):
            num = nums[i]
            
            if num>second:    #this means arr[i]<arr[j] and arr[j]<arr[k]
                return True
            
            elif num>first:     # this means arr[i]<num so we set it to second hoping we could find a num greater than second
                second = num
                
            else:               # this means num is the smallest one we set it to first
                first = num
        return False        