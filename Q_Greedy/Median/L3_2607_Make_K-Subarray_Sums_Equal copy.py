""" https://leetcode.com/problems/make-k-subarray-sums-equal/
grouping + greedy median + bezout's
"""
from header import *


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # bezout's lemma to find repeat cycle length
        k = gcd(k, len(arr))
        ans = 0
        for i in range(k):
            # grouping
            b = sorted(arr[i::k])
            # greedy median find minimum cost
            mid = b[len(b) // 2]
            ans += sum(abs(x - mid) for x in b)
        return ans


"""
[1,4,1,3]
2
[2,5,5,7]
3
"""
