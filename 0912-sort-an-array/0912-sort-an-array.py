class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        time complexity  --> O(nlogn)
        """
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

    
    """
    time complexity --> O(n2)
    """
    
    
#         def insert(nums,temp):
            
#             if len(nums)==0 or nums[-1]<=temp:
#                 nums.append(temp)
#                 return
            
#             val = nums[-1]
#             nums.pop()
#             insert(nums,temp)
#             nums.append(val)
        
#         if len(nums)==1:
#             return nums
        
#         temp = nums[-1]
#         nums.pop()
#         self.sortArray(nums)
#         insert(nums,temp)
#         return nums
        