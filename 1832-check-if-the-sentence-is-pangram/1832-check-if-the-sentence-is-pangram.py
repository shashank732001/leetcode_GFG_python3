class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        lookup = {}
        
        for i in sentence:
            lookup[i]=lookup.get(i,0)+1
        return len(lookup)==26    
            
        