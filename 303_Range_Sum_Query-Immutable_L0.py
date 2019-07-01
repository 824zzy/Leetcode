""" Naive
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])