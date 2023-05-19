""" https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
brute force to find all the valid subsequences and return the maximum one.
"""
class Solution:
    def removeDigit(self, A: str, d: str) -> str:
        ans = []
        for i, c in enumerate(A):
            if c==d:
                ans.append(A[:i]+A[i+1:])
        return max(ans)