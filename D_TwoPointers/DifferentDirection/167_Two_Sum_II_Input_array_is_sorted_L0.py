""" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Left pointer move right when sum is smaller then target
Right pointer move left when sum is larger then target

Time complexity: O(n)
"""
class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        l, r = 0, len(A)-1
        while l<r:
            if A[l]+A[r]==t: return [l+1, r+1]
            elif A[l]+A[r]<t: l += 1
            else: r -= 1