class Solution:
    def combinationSum4(self, nums: List[int], T: int) -> int:
        dp = [1] + [0]*T
        
        for i in range(1, T+1):
            for n in nums:
                if i-n>=0: dp[i] += dp[i-n]
        return dp[-1]