""" https://leetcode.com/problems/sort-array-by-parity/
Time: O(n), Space: O(1)
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A)-1
        while l<r:
            if not A[l]&1: l += 1
            elif A[r]&1: r -= 1
            else: A[l], A[r] = A[r], A[l]
        return A
        
# Time: O(n), Space: O(n)
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e, o = [], []
        for x in A:
            if x&1: o.append(x)
            else: e.append(x)
        return e+o