class Solution:
    def makeGood(self, s: str) -> str:
        def operation(strg):
            strg = list(strg)
            for i in range(len(strg)-1):
                # print(len(strg),i)
                if (strg[i]==strg[i+1].lower() or strg[i].lower()==strg[i+1]) and strg[i]!=strg[i+1]:
                    strg.pop(i)
                    strg.pop(i)
                    break
            # print(strg)        
            return "".join(strg)
        
        new_strg = operation(s)
        
        while new_strg!=s:
            s = new_strg
            new_strg = operation(s)
            # print(new_strg)
        return new_strg    