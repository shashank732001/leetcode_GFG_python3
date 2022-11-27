class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        carry = 0
        A = a[::-1]
        B = b[::-1]
        
        for i in range(max(len(A),len(B))):
            
            digitA = int(A[i]) if i<len(A) else 0
            digitB = int(B[i]) if i<len(B) else 0
            
            total = digitA + digitB + carry
            char = total%2
            carry = total//2
            res = res+str(char)
            
        if carry:
            res = res+"1"
        return res[::-1]    
            