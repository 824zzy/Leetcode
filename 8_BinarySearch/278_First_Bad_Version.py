""" L0: https://leetcode.com/problems/first-bad-version/
variance of template
"""
class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m): r = m - 1
            else: l = m + 1
        return l