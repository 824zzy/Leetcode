""" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Since the input array is sorted, binary search is also available besides two pointer.

Time complexity: O(nlogn)
"""
class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        ans = []
        for i, x in enumerate(A):
            y = t-x
            j = bisect_right(A, y)
            if A[j-1]==y: return (i+1, j)