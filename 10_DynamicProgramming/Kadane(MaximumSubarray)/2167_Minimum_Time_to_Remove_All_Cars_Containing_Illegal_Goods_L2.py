""" https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748424/Python-maximum-sum-on-subarray-explained
The most difficult part is how to translate the question into finding minimum subarray:

For left and right we paid just their lengths. For middle we pay twice number of ones se have inside, 
so we have: len(left) + 2* count(middle, 1) + len(right) 
            = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle) 
            = n + count(middle, 1) - count(middle, 0).
in fact what we need to found is the subarray with the smallest count(middle, 1) - count(middle, 0) value.
"""
class Solution:
    def minimumTime(self, s: str) -> int:
        A = [1 if i == "1" else -1 for i in s]
        ans, cur = inf, 0
        for x in A:
            cur = min(0, cur + x)
            ans = min(ans, cur)
        return len(A)+ans