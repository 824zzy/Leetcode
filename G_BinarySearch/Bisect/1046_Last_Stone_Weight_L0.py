""" https://leetcode.com/problems/last-stone-weight/
"""
class Solution:
    def lastStoneWeight(self, A: List[int]) -> int:
        A.sort()
        while len(A)>1:
            i = A.pop()
            j = A.pop()
            bisect.insort(A, abs(i-j))
        return A[0]