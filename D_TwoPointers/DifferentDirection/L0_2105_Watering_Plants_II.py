""" https://leetcode.com/problems/watering-plants-ii/
reading comprehension
"""
from header import *

class Solution:
    def minimumRefill(self, A: List[int], capa: int, capb: int) -> int:
        i, j = 0, len(A)-1
        a, b = capa, capb
        ans = 0
        while i<j:
            if A[i]<=a:
                a -= A[i]
            else:
                a = capa-A[i]
                ans += 1
            if A[j]<=b:
                b -= A[j]
            else:
                b = capb-A[j]
                ans += 1
            i += 1
            j -= 1
        if i==j: # when they meet in the middle
            x = max(a, b)
            ans += x<A[i]
        return ans