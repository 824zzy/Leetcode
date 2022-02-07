""" https://leetcode.com/problems/remove-duplicates-from-sorted-array/
copy A[j] to A[i] if A[j] is not seen yet
"""
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        i = 0
        for j in range(len(A)):
            if i==0 or A[j]!=A[i-1]:
                A[i] = A[j]
                i += 1
        return i