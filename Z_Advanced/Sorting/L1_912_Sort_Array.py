""" https://leetcode.com/problems/sort-an-array/
"""
from header import *

# Merge Sort: O(nlogn) under time limit


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            res = self.mergeSort(nums, 0, len(nums) - 1)
            return res

    def mergeSort(self, A, p, r):
        if p < r:
            q = (p + r) // 2
            self.mergeSort(A, p, q)
            self.mergeSort(A, q + 1, r)
            self.merge(A, p, q, r)
            return A

    def merge(self, A, p, q, r):
        n1, n2 = q - p + 1, r - q
        L, R = [A[p + i] for i in range(n1)], [A[q + j + 1] for j in range(n2)]
        L += [float("inf")]
        R += [float("inf")]
        i, j = 0, 0
        for k in range(p, r + 1):
            if L[i] < L[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1


# Bubble Sort


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(1, len(nums)):
            i = j - 1
            while i >= 0 and nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1
                j -= 1
        return nums


# Insert Sort: O(n^2)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(1, len(nums)):
            i, key = j - 1, nums[j]
            while i >= 0 and nums[i] > key:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = key
        return nums
