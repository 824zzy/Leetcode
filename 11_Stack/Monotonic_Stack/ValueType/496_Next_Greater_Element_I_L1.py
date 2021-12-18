""" L1: https://leetcode.com/problems/next-greater-element-i/
build a next greater hash table by monotonic decreasing stask.
"""
class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        stk, M = [], {}
        for n in B:
            while stk and stk[-1]<n:
                M[stk.pop()] = n
            stk.append(n)
        
        return [M.get(x, -1) for x in A]