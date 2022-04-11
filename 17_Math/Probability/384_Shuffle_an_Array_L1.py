""" https://leetcode.com/problems/shuffle-an-array/
Knuth shuffle
"""
class Solution:
    def __init__(self, nums: List[int]):
        self.A = nums
        self.orig = nums.copy()
        

    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        for i in range(1, len(self.A)): 
            ii = randint(0, i)
            self.A[ii], self.A[i] = self.A[i], self.A[ii]
        return self.A

# or cheating
class Solution:
    def __init__(self, nums: List[int]):
        self.A = nums
        self.orig = nums.copy()
        
    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        shuffle(self.A)
        return self.A