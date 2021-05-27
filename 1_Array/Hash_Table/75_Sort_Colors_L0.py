""" Not the optimal one since extra space usage
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        cnt = sorted(cnt.items(), key=lambda x: x[0])
        ans = []
        for c in cnt: ans.extend([c[0]]*c[1])
        nums[:] = ans