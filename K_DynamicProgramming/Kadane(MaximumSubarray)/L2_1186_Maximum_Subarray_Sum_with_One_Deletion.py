""" https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/1155630/Python3-bottom-up-dp
"""


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = d0 = d1 = -inf
        for x in arr:
            d0, d1 = max(x, x + d0), max(d0, x + d1)
            ans = max(ans, d0, d1)
        return ans
