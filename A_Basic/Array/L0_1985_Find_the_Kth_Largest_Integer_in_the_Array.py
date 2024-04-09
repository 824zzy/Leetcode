""" https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
1. convert array elements to int
2. sort array to find kth largest element
"""


class Solution:
    def kthLargestNumber(self, A: List[str], k: int) -> str:
        return sorted(A, key=int, reverse=True)[k - 1]
