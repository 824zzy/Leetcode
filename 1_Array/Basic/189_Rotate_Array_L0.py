class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # nums = [1, 2]  k = 3
        nums[:] = nums[-k:] + nums[:-k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(1, k+1):
            nums.insert(0, nums[-1])
            nums.pop()