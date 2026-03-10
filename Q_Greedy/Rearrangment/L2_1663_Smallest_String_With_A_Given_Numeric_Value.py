""" https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
1. generate the initial string with all 'a' characters. This will reduce k by n
2. try to turn rightmost 'a' into as larger characters as possible based on the remained k
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ["a"] * n
        k -= n
        while k:
            n -= 1
            val = min(25, k)
            ans[n] = chr(ord("a") + val)
            k -= val
        return "".join(ans)
