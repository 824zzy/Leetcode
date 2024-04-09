""" https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
translate the problem to count unique elements except 0
"""


class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        return len(set(A) - {0})

# or dumb simulation


class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for i in range(len(A)):
            if A[i] == 0:
                continue
            for j in range(i + 1, len(A)):
                A[j] -= A[i]
            ans += 1
            if A[-1] <= 0:
                return ans
        return ans
