""" https://leetcode.com/problems/next-greater-element-i/
build a next greater hash table by monotonic decreasing stask.

496: https://leetcode.com/problems/next-greater-element-i/
503: https://leetcode.com/problems/next-greater-element-ii/
556: https://leetcode.com/problems/next-greater-element-iii/
"""
from header import *


class Solution:
    def nextGreaterElement(self, B: List[int], A: List[int]) -> List[int]:
        mp = defaultdict(lambda: -1)
        stk = []

        for i in range(len(A)):
            while stk and A[stk[-1]] < A[i]:
                mp[A[stk.pop()]] = A[i]
            stk.append(i)
        return [mp[x] for x in B]
