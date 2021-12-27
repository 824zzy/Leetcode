""" L0: prefix sum array for query
"""
class NumArray:
    def __init__(self, nums: List[int]):
        self.P = [0]
        prefix = 0
        for n in nums:
            prefix += n
            self.P.append(prefix)
        
    def sumRange(self, l: int, r: int) -> int:
        return self.P[r+1]-self.P[l]
