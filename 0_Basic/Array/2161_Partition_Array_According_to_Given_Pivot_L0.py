""" https://leetcode.com/problems/partition-array-according-to-given-pivot/
simply use pivot to divide array into three parts: less(a), large(b), equal()
"""
class Solution:
    def pivotArray(self, A: List[int], pivot: int) -> List[int]:
        a, b, c = [], [], []
        for x in A:
            if x<pivot: a.append(x)
            elif x>pivot: b.append(x)
            else: c.append(x)
        return a+c+b