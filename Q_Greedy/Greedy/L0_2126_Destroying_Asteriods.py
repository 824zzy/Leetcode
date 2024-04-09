""" https://leetcode.com/problems/destroying-asteroids/
greedily add mass until find a large one
"""


class Solution:
    def asteroidsDestroyed(self, n: int, A: List[int]) -> bool:
        A.sort()
        for i in range(len(A)):
            if n >= A[i]:
                n += A[i]
            else:
                return False
        return True
