""" https://leetcode.com/problems/reverse-vowels-of-a-string/
basic usage of two pointer
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r, s = 0, len(s) - 1, list(s)
        while l < r:
            while l < r and s[l] not in "aeiouAEIOU":
                l += 1
            while l < r and s[r] not in "aeiouAEIOU":
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
