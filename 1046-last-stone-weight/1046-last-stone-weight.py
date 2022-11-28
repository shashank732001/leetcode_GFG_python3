class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        python doesn't have maxheap 
        
        so we use min heap and multiply every value with -1 so our max value becomes the             minimum one 
        
        """
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        # print(stones)
        while len(stones)>1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one<two:
                heapq.heappush(stones,-1*(two-one))
            
            # print(one,two)    
        if stones:
            return stones[0] if stones[0]>0 else -1*stones[0]
        return 0
            
                