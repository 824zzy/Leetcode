""" https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
from godv:
count zeros, when meet "1" then we need at least "ans+1" seconds but less than zeros count seconds.
      0110101
zeros:1112233
ans  :0122334
"""


class Solution:
    def secondsToRemoveOccurrences(self, A: str) -> int:
        ans = 0
        zeros = 0
        for i in range(len(A)):
            if A[i] == '0':
                zeros += 1
            if A[i] == '1' and zeros:
                ans = max(ans + 1, zeros)
        return ans

# simple simulation since n<=1000, time complexity O(n^2)


class Solution:
    def secondsToRemoveOccurrences(self, A: str) -> int:
        A = list(A)
        f = True
        ans = 0
        while f:
            i = 0
            f = False
            while i < len(A) - 1:
                if A[i] == '0' and A[i + 1] == '1':
                    f = True
                    A[i], A[i + 1] = A[i + 1], A[i]
                    i += 1
                i += 1
            if f:
                ans += 1
        return ans
