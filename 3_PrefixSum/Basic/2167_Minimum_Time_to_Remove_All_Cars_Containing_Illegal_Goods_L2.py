""" https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748452/Python-Explanation-with-pictures.-Prefix-and-Suffix.
1. We assume that the maxCost is the cost that removing all illegal cars with a cost of 2, no matter where they are.
2. Then, we would like to save some costs, by removing cars from one side, with a cost of 1.
"""
class Solution:
    def minimumTime(self, s: str) -> int:
        A = [1 if i == "1" else -1 for i in s]
        ans, cur = inf, 0
        for x in A:
            cur = min(0, cur + x)
            ans = min(ans, cur)
        return len(A)+ans