# BIT
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = len(nums)
        self.c = [0] * (self.l+1)
        for i, n in enumerate(nums):
            j = i + 1
            while j<=self.l:
                self.c[j] += nums[i]
                j += j & (-j)
        
    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i<=self.l:
            self.c[i] += delta
            i += i & -i
    
    def get(self, i: int) -> int:
        i += 1
        ans = 0
        while i>0:
            ans += self.c[i]
            i -= i & -i
        return ans

    def sumRange(self, i: int, j: int) -> int:
        return self.get(j)-self.get(i-1)
    
    
# Straightforward 
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        
    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)