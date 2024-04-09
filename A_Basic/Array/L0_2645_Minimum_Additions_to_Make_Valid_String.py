""" https://leetcode.com/problems/minimum-additions-to-make-valid-string/
"""
# count the all the cycles, the additions are 3*t-len(s)


class Solution:
    def addMinimum(self, s: str) -> int:
        t = 1
        for i in range(1, len(s)):
            if s[i - 1] >= s[i]:
                t += 1
        return 3 * t - len(s)

# count cycles one by one and update the answer on the fly


class Solution:
    def addMinimum(self, word: str) -> int:
        i = 0
        ans = 0
        while i < len(word):
            if i + 2 < len(word) and word[i:i + 3] == 'abc':
                i += 3
            elif i + 1 < len(word) and word[i:i + 2] in ('ab', 'ac', 'bc'):
                i += 2
                ans += 1
            else:
                i += 1
                ans += 2
        return ans


"""
"b"
"aaa"
"abc"
"aaaaac"
"""
