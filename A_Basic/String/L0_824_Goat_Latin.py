""" https://leetcode.com/problems/goat-latin/
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        ans = ''

        for i, e in enumerate(S.split()):
            if e[0] in vowel:
                ans += e + 'ma' + 'a' * (i + 1) + ' '
            else:
                ans += e[1:] + e[0] + 'ma' + 'a' * (i + 1) + ' '
        return ans[:-1]
