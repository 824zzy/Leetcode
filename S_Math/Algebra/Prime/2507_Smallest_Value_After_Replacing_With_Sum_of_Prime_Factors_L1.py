""" https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/
n decreases logarithmically, allowing you to simulate the process.
"""
class Solution:
    def smallestValue(self, n: int) -> int: 
        while 1:
            sm = 0
            nn = n
            for f in range(2, nn+1):
                while (nn%f)==0:
                    nn //= f
                    sm += f
            if sm==n: break
            n = sm
        return n