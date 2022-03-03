""" https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
refer to: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1292744/Python3-freq-tables
We have to use bottom up dp since we use hash table as states
"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        dp = [defaultdict(int) for _ in range(len(A))]
        
        for i in range(len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                ans += dp[j].get(diff, 0)
                dp[i][diff] += 1+dp[j][diff]
        return ans