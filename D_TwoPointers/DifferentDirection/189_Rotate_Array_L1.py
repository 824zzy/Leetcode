""" https://leetcode.com/problems/rotate-array/submissions/
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
                A[l], A[r] = A[r], A[l]
                l, r = l+1, r-1
        swap(0, len(A)-1)
        swap(0, k-1)
        swap(k, len(A)-1)
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # nums = [1, 2]  k = 3
        nums[:] = nums[-k:] + nums[:-k]