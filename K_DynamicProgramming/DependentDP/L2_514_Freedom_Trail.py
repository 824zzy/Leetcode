""" https://leetcode.com/problems/freedom-trail/
deal with the ring as a circle, and the key as a sequence
"""
from header import *


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dp(i, cur):
            if i == len(key):
                return 0
            ans = inf
            for j in range(cur, cur+len(ring)):
                # ensure the index is in the range
                j %= len(ring)
                if ring[j] == key[i]:
                    # the minimum distance can be clockwise or counter-clockwise
                    d = abs(j-cur)
                    ans = min(ans, min(d, len(ring)-d)+1 + dp(i+1, j))
            return ans

        return dp(0, 0)


"""
"godding"
"gd"
"godding"
"godding"
"goding"
"goding"
"abcde"
"ade"
"""
