import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k]
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:heapq.heappop(heap)
        return heap[0]        
        
        