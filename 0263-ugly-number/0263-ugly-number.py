class Solution:
    def isUgly(self, n: int) -> bool:
        ugly_prime = [2,3,5]
        
        if n<=0:
            return False
        
        def no_ugly(n,ugly_no):
            
            while n%ugly_no==0:

                n = n//ugly_no
            return n
        
        for i in ugly_prime:
            n = no_ugly(n,i)
        
        
        return True if n==1 else False
                    
                
        