class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        print(s)
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                res.append(s[i])
        return " ".join(res)