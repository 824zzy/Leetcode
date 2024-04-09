""" https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
optimize step by step
"""
from header import *

# array brute force


class SparseVector:
    def __init__(self, nums: List[int]):
        self.A = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(x * y for x, y in zip(self.A, vec.A))

# hash table for spare storage


class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {i: x for i, x in enumerate(nums)}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k, v in self.mp.items():
            if k in vec.mp:
                ans += v * vec.mp[k]
        return ans

# two pointer to reduce the time complexity


class SparseVector:
    def __init__(self, nums: List[int]):
        self.A = tuple((i, x) for i, x in enumerate(nums) if x)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = 0
        ans = 0
        for j in range(len(vec.A)):
            while i < len(self.A) and self.A[i][0] < vec.A[j][0]:
                i += 1
            if i < len(self.A) and self.A[i][0] == vec.A[j][0]:
                ans += self.A[i][1] * vec.A[j][1]
        return ans

# binary search when one array is not sparse


class SparseVector:
    def __init__(self, nums: List[int]):
        self.A = tuple((i, x) for i, x in enumerate(nums) if x)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i in range(len(vec.A)):
            j = bisect_left(self.A, (vec.A[i][0], -inf))
            if j < len(self.A) and vec.A[i][0] == self.A[j][0]:
                ans += vec.A[i][1] * self.A[j][1]
        return ans


"""
[1,0,0,2,3]
[0,3,0,4,0]
[0,1,0,0,0]
[0,0,0,0,2]
[0,1,0,0,2,0,0]
[1,0,0,0,3,0,4]
[5,0,0,0,0,0,0,0,0,0,0,0,0]
[0,0,0,0,0,0,0,0,0,5,4,0,3]
[0,0,0,0,0,0,3,0,0,3,0,0,0]
[0,0,2,0,0,4,3,0,0,2,0,0,0]
"""
