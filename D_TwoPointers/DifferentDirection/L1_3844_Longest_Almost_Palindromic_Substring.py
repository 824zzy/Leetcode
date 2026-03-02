""" https://leetcode.com/problems/longest-almost-palindromic-substring/
Expand-around-center with one-skip extension (similar to LC 680).

For each center, expand the palindrome until mismatch at (l, r). Then try
two branches: skip left char (expand from l-1, r) or skip right char (expand
from l, r+1). The longer result is the almost-palindromic substring length.
O(n^2) time.
"""


class Solution:
    def almostPalindromic(self, s: str) -> int:
        def pal(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r

        ans = 0
        for i in range(2 * (len(s)) - 1):
            l, r = pal(i // 2, (i + 1) // 2)
            ll, rr = pal(l - 1, r)
            ans = max(ans, rr - ll - 1)
            ll, rr = pal(l, r + 1)
            ans = max(ans, rr - ll - 1)
            if ans >= len(s):
                return ans
        return ans
