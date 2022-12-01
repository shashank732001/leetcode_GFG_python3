class Solution:
    def halvesAreAlike(self, s: str) -> bool:
#         mid = len(s)//2
#         a = s[:mid]
#         b = s[mid:]
#         count1 = 0
#         count2 = 0
        
#         for i in range(mid):
#             if a[i] in "aeiouAEIOU":
#                 count1+=1
                
#             if b[i] in "aeiouAEIOU":
#                 count2+=1
#         return count1==count2      

        n = len(s)
        mid = n//2
        count1 = 0
        count2 = 0
        i = mid-1
        j = mid
        
        while i>=0 and j<n:
            if s[i] in "aeiouAEIOU":
                count1+=1
                
            if s[j] in "aeiouAEIOU":
                count2+=1
                
            i-=1
            j+=1
            
        return count1==count2    
            
        
                