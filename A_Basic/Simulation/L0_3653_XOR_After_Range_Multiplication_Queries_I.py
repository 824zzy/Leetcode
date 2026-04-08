""" https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
Brute-force simulation: for each query (l, r, k, v), step i from l to r by k
and multiply nums[i] by v mod 1e9+7. Finally XOR all elements together.
n, q <= 1000 so the inner walk is at most ~1000 steps per query.
"""


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        return reduce(xor, nums)
