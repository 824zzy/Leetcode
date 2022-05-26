""" https://leetcode.com/problems/remove-element/
copy A[j] to A[i] if A[j]!=val
"""
class Solution:
    def removeElement(self, A: List[int], val: int) -> int:
        i = 0
        for j in range(len(A)):
            if A[j]!=val:
                A[i] = A[j]
                i += 1
        return i