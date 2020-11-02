"""
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp1 = [1] * len(nums) # longest subsequence ending at index j
        for j in range(1, len(nums)):
            temp = []
            for i in range(j):
                if nums[i] < nums[j]:
                    temp.append(1+dp1[i])
            dp1[j] = max(temp or [1])
        
        dp2 = [0] * len(nums)
        for j in range(len(nums)):
            if dp1[j] == 1:
                dp2[j] = 1
            else:
                temp = []
                for i in range(j):
                    if nums[i] < nums[j] and dp1[i]+1 == dp1[j]:
                        temp.append(dp2[i])
                dp2[j] = sum(temp)
        m = max(dp1 or [0])
        
        ans = []
        for i in range(len(nums)):
            
            if dp1[i] == m:
                ans.append(dp2[i])
        return sum(ans or [0])