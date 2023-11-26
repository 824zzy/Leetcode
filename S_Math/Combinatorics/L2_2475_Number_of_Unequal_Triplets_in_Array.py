""" https://leetcode.com/problems/number-of-unequal-triplets-in-array/
learned from godv: https://leetcode.com/problems/number-of-unequal-triplets-in-array/solutions/2831702/o-n/

1. count the frequency of each number
2. use the formula to calculate the number of unequal triplets: sum(m[0]...m[j - 1]) * m[j] * sum(m[j + 1]...m[n - 1])

E.g. [1,1,2,2,2,3,3,3,3,4,4,4,4,4] => mp=[2,3,4,5], then the unique triplets are:
2*3*4 + 2*3*5 + 2*4*5 + 3*4*5 === 2*3*(4+5) + (2+3)*4*5

time complexity: O(n)
"""
from header import *

class Solution:
    def unequalTriplets(self, A: List[int]) -> int:
        mp = Counter(A)
        l, r = 0, len(A)
        ans = 0
        for _, v in mp.items():
            r -= v
            ans += l*v*r
            l += v
        return ans