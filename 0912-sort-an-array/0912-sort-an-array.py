class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums)>1:
            left_array = nums[:len(nums)//2]
            right_array = nums[len(nums)//2:]
            
            self.sortArray(left_array)
            self.sortArray(right_array)
            
            i = 0 
            j = 0
            k = 0
            
            while i<len(left_array) and j<len(right_array):
                if left_array[i]<right_array[j]:
                    nums[k]=left_array[i]
                    i+=1
                    k+=1
                else:
                    nums[k]=right_array[j]
                    j+=1
                    k+=1
            while i<len(left_array):
                nums[k]=left_array[i]
                i+=1
                k+=1
            
            while j<len(right_array):
                nums[k]=right_array[j]
                j+=1
                k+=1
        return nums        