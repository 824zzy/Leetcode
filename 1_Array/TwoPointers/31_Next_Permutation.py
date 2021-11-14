""" L2: https://leetcode.com/problems/next-permutation/
https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
2. Find the largest index l greater than k such that a[k] < a[l].
3. Swap the value of a[k] with that of a[l].
4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1: return
        k = len(nums)-2
        while k>-1:
            if nums[k]<nums[k+1]: # largest A[k]<A[k+1]
                l = len(nums)-1
                while l>k:
                    if nums[k]<nums[l]: # largest A[k]<A[l]
                        nums[k], nums[l] = nums[l], nums[k] # swap A[k], A[l]
                        nums[k+1:] = nums[k+1:][::-1] # reverse A[k+1:]
                        return
                    else: l -= 1
            else: k -= 1
        nums.reverse() # corner case: [3,2,1]