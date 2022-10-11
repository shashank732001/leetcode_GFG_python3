class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resdict = defaultdict(list)
        for i in strs:
            count =[0]*26  # 26 because a.....z
            for j in i :
                count[ord(j)-ord("a")]+=1
                
            resdict[tuple(count)].append(i)
        return resdict.values()   