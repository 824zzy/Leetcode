class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(reversed(s)):
            ans += (ord(c) - 64) * 26 ** i
        return ans
