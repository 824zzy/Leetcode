""" https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
"""


class Solution:
    def digitCount(self, A: str) -> bool:
        cnt = Counter(A)
        return all([cnt[str(i)] == int(A[i]) for i in range(len(A))])
