class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

# 5/*/2019
class Solution:
    def reverseWords(self, s: str) -> str:
        split_l = s.split()
        reverse_l = [i for i in split_l[::-1]]
        
        res = ''
        for w in reverse_l:
            res += w + ' '
        
        return res[:-1]