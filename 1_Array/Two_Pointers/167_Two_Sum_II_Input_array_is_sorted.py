""" L0: two pointer template
Left pointer move right when sum is smaller then target
Right pointer move left when sum is larger then target
"""
class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        l, r = 0, len(A)-1
        while l<=r:
            if A[l]+A[r]==target:
                return [l+1, r+1]
            elif A[l]+A[r]<target:
                l += 1
            else:
                r -= 1