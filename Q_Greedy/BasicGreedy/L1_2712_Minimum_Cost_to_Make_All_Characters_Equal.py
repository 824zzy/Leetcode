""" https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
find the conclusion:
f'(0) = f(1) + min(i+1, n-i-1)
f'(1) = f(0) + min(i+1, n-i-1)
"""
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = {0: 0, 1: 0}
        for i in range(n):
            if s[i]=='0':
                ans[1] = ans[0]+min(i+1, n-i-1)
            else:
                ans[0] = ans[1]+min(i+1, n-i-1)
        return min(ans[0], ans[1])