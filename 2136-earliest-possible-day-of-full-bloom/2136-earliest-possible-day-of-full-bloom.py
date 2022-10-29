class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        bloom = list(zip(plantTime,growTime))
        bloom.sort(key=lambda x:x[1],reverse = True)
        start = 0
        res = 0
        # print(bloom)
        for plant,grow in bloom:
            start+=plant
            res = max(res,start+grow)
        return res    