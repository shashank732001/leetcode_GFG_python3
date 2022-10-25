class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         str1 = ""
#         str2 = ""
#         for i in word1:
#             str1+=i
            
#         for i in word2:
#             str2+=i

        str1 = "".join(word1)
        str2 = "".join(word2)
        return str1==str2    