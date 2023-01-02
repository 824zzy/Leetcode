""" https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/
greedily take as much characters as possible to the summation
"""
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        sm = 0
        for x in s:
            if sm*10+int(x)<=k:
                sm = sm*10+int(x)
            elif int(x)<=k:
                sm = int(x)
                ans += 1
            else:
                return -1
        return ans+1