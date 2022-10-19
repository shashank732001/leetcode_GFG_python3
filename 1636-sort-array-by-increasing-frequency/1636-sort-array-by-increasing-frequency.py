class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        lookup = {}
        for i in nums:
            lookup[i] = lookup.get(i,0)+1
        
        sort_dic = sorted(sorted(lookup,reverse=True),key=lookup.get)
        res = []
        for i in sort_dic:
            res.extend([i] * lookup[i])
        return res    
            