""" https://leetcode.com/problems/largest-3-same-digit-number-in-string/
use groupby to find same digit continuous sequence then find the maximal sequence whose length is larger than one

Time: O(n)
"""
class Solution:
    def largestGoodInteger(self, A: str) -> str:
        A = [[k, len(list(v))] for k, v in groupby(num)]
        ans = ''
        for k, v in A:
            if v>=3: ans = max(ans, k*3)
        return ans