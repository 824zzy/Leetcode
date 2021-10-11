"""L0: https://leetcode.com/problems/rotate-array/submissions/
two pointer swap for three times
"""
class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(A)
        def swap(l, r):
            while l<r:
                # print(l, r)
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
            
        l, r = 0, len(A)-1
        swap(l, r)
        l, r = 0, k-1
        swap(l, r)
        l, r = k, len(A)-1
        swap(l, r)
        
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