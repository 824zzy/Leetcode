""" https://leetcode.com/problems/arithmetic-slices/submissions/
It is a little special dp problem.
For each x in A, count it has how many continuously arithmetic slices
dp[i] means how many arithemetic slices till nums[i]
"""
# top down
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i+1<len(A) and A[i]-A[i-1]==A[i+1]-A[i]: 
                return 1+dp(i+1)
            else: return 0
        
        return sum([dp(i) for i in range(1, len(A)-1)])
    
# bottom up
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cnt = 0
        ans = 0
        for i in range(1, len(A)-1):
            if A[i]-A[i-1]==A[i+1]-A[i]: cnt += 1
            else: cnt = 0
            ans += cnt
        return ans