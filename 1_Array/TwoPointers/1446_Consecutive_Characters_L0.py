class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        ans = 0
        for r in range(1, len(s)):
            if s[r]==s[l]:
                ans = max(ans, r-l+1)
            else:
                l = r
        return max(ans, 1)