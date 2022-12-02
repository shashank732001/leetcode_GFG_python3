class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        
        lookup1 = {}
        lookup2 = {}
        
        for i in range(len(word1)):
            
            lookup1[word1[i]] = 1 + lookup1.get(word1[i],0)
            lookup2[word2[i]] = 1 + lookup2.get(word2[i],0)
        
        # print(lookup1,lookup2)
        val1 = sorted(lookup1.values())
        val2 = sorted(lookup2.values())
        # print(val1,val2)
        key1 = lookup1.keys()
        key2 = lookup2.keys()
        
        return key1==key2 and val1==val2