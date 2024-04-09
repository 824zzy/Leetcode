""" https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
represent set as bit mask
"""
from header import *


class Solution:
    def findThePrefixCommonArray(
            self,
            A: List[int],
            B: List[int]) -> List[int]:
        setA, setB = 0, 0
        ans = [0] * len(A)
        for i, (x, y) in enumerate(zip(A, B)):
            setA |= 1 << x
            setB |= 1 << y
            ans[i] = (setA & setB).bit_count()
        return ans


class Solution:
    def findThePrefixCommonArray(
            self,
            A: List[int],
            B: List[int]) -> List[int]:
        setA, setB = set(), set()
        ans = [0] * len(A)
        for i, (x, y) in enumerate(zip(A, B)):
            setA.add(x)
            setB.add(y)
            ans[i] = len(setA & setB)
        return ans
