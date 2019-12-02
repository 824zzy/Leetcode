class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans, cnt = 1, 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                cnt += 1
            else:
                ans, cnt = max(ans, cnt), 1
        return max(ans, cnt)