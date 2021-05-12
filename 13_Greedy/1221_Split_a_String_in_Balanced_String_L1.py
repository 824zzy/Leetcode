"""
"""
class Solution:
    def balancedStringSplit(self, S: str) -> int:
        cnt = 0
        ans = 0
        for s in S:
            if s=='L': cnt += 1
            else: cnt -= 1
            if cnt==0: ans += 1
        return ans