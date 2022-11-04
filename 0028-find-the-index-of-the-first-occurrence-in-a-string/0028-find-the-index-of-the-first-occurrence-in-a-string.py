class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)          #cheat code
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        i = 0                               #pointer for starting index
        if needle_len == 0:return 0         # given condition
        while i+needle_len<=haystack_len:    #iterate till last element in haystack
            if haystack[i:i+needle_len] == needle:        #checking the condition
                return i                         #return the current index
            i+=1                                 # incrementing the index
        return -1                               # return -1 if needle is not in haystack
            
        