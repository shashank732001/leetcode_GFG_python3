class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        n = len(count)
        occur = set()
        for key, val in count.items():
            occur.add(val)
        return n==len(occur)    
            
            