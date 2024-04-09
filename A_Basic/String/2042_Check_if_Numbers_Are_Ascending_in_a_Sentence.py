""" L0: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
split string and count numeric substring.
"""


class Solution:
    def areNumbersAscending(self, S: str) -> bool:
        A = [int(s) for s in S.split() if s.isnumeric()]
        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:
                return False
        return True
