class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = "".join(str(i) for i in num)
        num1 = int(num)
        res = [i for i in str(num1+k)]
        return res
        