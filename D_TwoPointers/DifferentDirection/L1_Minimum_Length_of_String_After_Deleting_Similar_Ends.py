""" https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
two pointer greedy. Be aware of some edge cases.
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            c = s[l]
            while l <= r and s[l] == c:
                l += 1
            while l <= r and s[r] == c:
                r -= 1
        return r - l + 1


"""
"ca"
"cabaabac"
"aabccabba"
"bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
"""
