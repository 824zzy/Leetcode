""" https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
check each row and column's set
"""


class Solution:
    def checkValid(self, A: List[List[int]]) -> bool:
        for a, b in zip(A, zip(*A)):
            if len(set(a)) != len(A[0]) or len(set(b)) != len(A):
                return False
        return True
