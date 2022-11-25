class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashmap= {}
        # for i in nums:
        #     hashmap[i]=1+hashmap.get(i,0)
        #     if hashmap[i]>1:
        #         return i
        # print(newlist)
        
        slow  = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
                
        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                return slow