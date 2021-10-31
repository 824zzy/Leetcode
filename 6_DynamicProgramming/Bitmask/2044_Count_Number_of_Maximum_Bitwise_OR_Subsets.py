""" L1: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
bitmask template
"""
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * (1<<N)
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                if mask & (1<<j):
                    neib = dp[mask ^ (1<<j)]
                    dp[mask] = neib|nums[j]
        return dp.count(max(dp))
    
# dictionary dp from lee215: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution
class Solution:
    def countMaxOrSubsets(self, A):
        dp = collections.Counter([0])
        for a in A:
            for k, v in dp.items():
                dp[k | a] += v
        return dp[max(dp)]