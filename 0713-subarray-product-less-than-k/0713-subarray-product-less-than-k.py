class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product_so_far = 1
        mini = 0
        count = 0 
        total = 0
        n = len(nums)
        
        for i in range(n):
            # we compute product so far and increment count
            product_so_far *=nums[i]
            count+=1
            
            #if our productsofar is greater  than k we move mini and make sure it doesnt pass i
            
            while product_so_far>=k and mini<=i:
                
                product_so_far /= nums[mini]
                mini+=1
                count-=1
                
            # if product_so_far<k:
            total+=count
        return total        