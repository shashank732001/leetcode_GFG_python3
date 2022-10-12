class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        stack = []
        n = len(nums2)
        
        for i in range(n-1,-1,-1):
            
            if not stack and nums2[i] in nums1:
                res[nums1.index(nums2[i])] = -1
                
            elif stack and stack[-1]>nums2[i] and nums2[i] in nums1:
                res[nums1.index(nums2[i])] = stack[-1]
            
            else:
                while stack and stack[-1]<=nums2[i]:
                    stack.pop()
                    
                    
                if stack and nums2[i] in nums1:
                    res[nums1.index(nums2[i])] = stack[-1]
                elif not stack and nums2[i] in nums1:
                    res[nums1.index(nums2[i])] = -1
            stack.append(nums2[i])
        return res    
                    