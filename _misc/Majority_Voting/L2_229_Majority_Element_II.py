""" https://leetcode.com/problems/majority-element-ii/
"""
from header import *

# Boyer-Moore Vote Algorithm


class Solution:
    def majorityElement(self, A: List[int]) -> List[int]:
        a, b = [None, 0], [None, 0]
        for i in range(len(A)):
            x = A[i]
            if x == a[0]:
                a[1] += 1
            elif x == b[0]:
                b[1] += 1
            else:
                if a[1] == 0:
                    a = [x, 1]
                elif b[1] == 0:
                    b = [x, 1]
                else:
                    a[1], b[1] = a[1] - 1, b[1] - 1
        return set([x for x in (a[0], b[0]) if A.count(x) > len(A) // 3])
