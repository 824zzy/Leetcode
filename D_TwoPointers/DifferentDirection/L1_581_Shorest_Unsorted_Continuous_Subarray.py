""" https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
1. sort the array
2. find left&right most different elements by two pointers

Time: O(nlogn) due to sort function
"""


class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        sorted_A = sorted(A)
        l, r = 0, len(A) - 1
        while l < r:
            if sorted_A[l] == A[l]:
                l += 1
            elif sorted_A[r] == A[r]:
                r -= 1
            else:
                break
        if l == r:
            return 0
        else:
            return r - l + 1
