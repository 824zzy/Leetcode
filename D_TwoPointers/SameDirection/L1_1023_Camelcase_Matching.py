""" https://leetcode.com/problems/camelcase-matching/
ij pointer
"""


class Solution:
    def camelMatch(self, Q: List[str], p: str) -> List[bool]:
        def isMatch(A):
            i = 0
            for j in range(len(A)):
                if i < len(p) and A[j] == p[i]:
                    i += 1
                elif A[j].isupper():
                    return False
            if i == len(p):
                return True

        return [isMatch(q) for q in Q]
