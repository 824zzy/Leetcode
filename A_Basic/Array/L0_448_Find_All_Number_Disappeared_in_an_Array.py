""" https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
negative encoding: use A as extra space
"""
class Solution:
    def findDisappearedNumbers(self, A: List[int]) -> List[int]:
        for x in A:
            if A[abs(x)-1]>0: A[abs(x)-1] *= -1
        return [i+1 for i, a in enumerate(A) if a>0]