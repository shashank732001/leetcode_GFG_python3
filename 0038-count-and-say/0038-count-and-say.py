class Solution:
    def countAndSay(self, n: int) -> str:
        num ="1"
        
        def next_member(num):
            i = 0
            res =[]
            while i<len(num):
                count=1
                while i+1<len(num) and num[i]==num[i+1]:
                    count+=1
                    i+=1
                res.append(str(count)+num[i])
                i+=1
            return "".join(res)
        
        for _ in range(n-1):
            num = next_member(num)
        return num    