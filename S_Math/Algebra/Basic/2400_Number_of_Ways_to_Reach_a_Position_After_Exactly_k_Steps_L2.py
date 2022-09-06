""" https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
learn from lee: https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/discuss/2527381/JavaC%2B%2BPython-Math-Solution-O(klogk)

there are three conditions:
1. we cannot go from s to e in k steps because k is too small
2. we cannot go from s to e in k steps because we need one more step
3. we can go from s to e in k steps, then we need to pick right steps from k steps to go right
"""
from header import *
class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        if k-abs(s-e)<0:
            return 0
        if (s-e-k)%2!=0: 
            return 0
        return comb(k, (e-s+k)//2)%(10**9+7)