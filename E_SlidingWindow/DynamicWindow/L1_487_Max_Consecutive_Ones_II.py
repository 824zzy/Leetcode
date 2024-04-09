""" https://leetcode.com/problems/max-consecutive-ones-ii/
typical sliding window
"""
from header import *


class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        zero_cnt = 0
        i = 0
        ans = 0
        for j in range(len(A)):
            zero_cnt += A[j] == 0
            while zero_cnt > 1:
                zero_cnt -= A[i] == 0
                i += 1
            ans = max(ans, j - i + 1)
        return ans


# greedy simulation solution
class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        A = [(i, len(list(x))) for i, x in groupby(A)]

        ans = 1
        for i, (x, l) in enumerate(A):
            # cannot flip
            if x == 1:
                ans = max(ans, l + (i + 1 < len(A) or i - 1 >= 0))
            # can flip
            if x == 0 and l == 1:
                l = A[i - 1][1] if i else 0
                r = A[i + 1][1] if i + 1 < len(A) else 0
                ans = max(ans, l + r + 1)
        return ans


"""
[1,0,1,1,0]
[1,0,1,1,0,1]
[0,1,1,1]
[1]
[0,0]
[1,1,1,0,0]
"""
