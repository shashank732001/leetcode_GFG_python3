class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0                       # i is changing pointer
        for j in nums:            
            if j!=val:            # j is reading pointer
                nums[i]=j         # placing all elements except val 
                i+=1
        return i        
            