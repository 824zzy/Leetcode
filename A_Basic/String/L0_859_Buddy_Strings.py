from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if Counter(A) != Counter(B):
            return False
        diff = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                diff += 1
            if diff > 2:
                return False
        return diff == 2 or sum(
            [v for k, v in Counter(A).items()]) > len(Counter(A).items())
