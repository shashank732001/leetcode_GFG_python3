class Solution:
    def intToRoman(self, num: int) -> str:
        rom = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000,
        }
        
        rom = {k:v for k,v in sorted(rom.items(),key = lambda x:x[1],reverse = True)}
        r = ""
        for k,v in rom.items():
            if num//v:
                count = num//v
                r+=(count*k)
                num = num%v

        return r        