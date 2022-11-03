class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = {}
        ans = 0
        center = False
        for item in words:
            word_dict[item] = word_dict.get(item, 0) + 1
        
        for item in word_dict:
            reverse = item[::-1]
            
            if item[0] == item[1]:
                if word_dict[item] % 2 == 0:
                    ans += word_dict[item]
                else:
                    ans += (word_dict[item] - 1)
                    center = True
            elif reverse in word_dict:
                    reverse_count = word_dict[reverse]
                    item_count = word_dict[item]
                    ans += min(reverse_count, item_count)

        if center:
            ans += 1
        
        return ans * 2