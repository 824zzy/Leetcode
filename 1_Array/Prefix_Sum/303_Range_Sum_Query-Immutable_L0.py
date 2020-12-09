class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        for i in range(len(nums)):
            self.prefix[i] = sum(nums[:i+1])

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j]-self.prefix[i-1] if i!=0 else self.prefix[j]
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])