class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lookup = {}
        res = []
        for i in words:
            lookup[i]=lookup.get(i,0)+1
        
        lookup = {k:v for k,v in sorted(lookup.items(),key=lambda x:x[0])}
        lookup = {k:v for k,v in sorted(lookup.items(),key=lambda x:x[1],reverse=True)}
        
        for key,val in lookup.items():
            if len(res)<k:
                res.append(key)
        return res        