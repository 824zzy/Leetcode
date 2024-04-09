class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i in range(len(nums)):
            while s and nums[i] < s[-1] and len(s) + len(nums) - i - 1 >= k:
                s.pop()
            if len(s) < k:
                s.append(nums[i])
        return s
