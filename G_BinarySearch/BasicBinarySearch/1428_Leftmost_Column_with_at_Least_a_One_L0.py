""" https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
brute force + binary search

Given 1000 calls limitation brute force will result in 100*log(100) = 1000 which is allowed
"""
from header import *

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def fn(i):
            l, r = 0, c
            while l<r:
                m = (l+r)//2
                if binaryMatrix.get(i, m)==1: r = m
                else: l = m+1
            return l
        
        r, c = binaryMatrix.dimensions()
        ans = [0]*r
        for i in range(r):
            ans[i] = fn(i)
        return min(ans) if min(ans)<c else -1