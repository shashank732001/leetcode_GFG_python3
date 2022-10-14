class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n==1 and k==1:
            return 0
        
        mid =pow(2,n-1)//2
        
        if k<=mid:
            return self.kthGrammar(n-1,k)
        
        else:
            ans = not self.kthGrammar(n-1,k-mid)
            return 1 if ans == True else 0