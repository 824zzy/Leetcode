""" https://leetcode.com/problems/valid-triangle-number/
1. A[i] + A[j] > A[k]
2. sort the array
3. when A[i]+A[j]>A[k]: (A[i], A[j]), (A[i+1], A[j]), ... (A[j-1], A[j]) are valid
4. update two pointers
"""
from header import *


class Solution:
    def triangleNumber(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for k in reversed(range(1, len(A))):
            i, j = 0, k - 1
            while i < j:
                if A[i] + A[j] > A[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


"""
[2,2,3,4]
[4,2,3,4]
"""
