""" https://leetcode.com/problems/k-diff-pairs-in-an-array/
Let us just use counter and count frequency of each number in our array. We can have two options:
1. k > 0, it means, that for each unique number i we are asking if number i+k also in table.
2. k = 0, it means, that we are looking for pairs of equal numbers, so just check each frequency.
"""
from header import *


class Solution:
    def findPairs(self, A: List[int], k: int) -> int:
        if k == 0:
            return sum(x > 1 for x in Counter(A).values())

        A.sort()
        seen = set()
        ans = 0
        for i, x in enumerate(A):
            if i and A[i] == A[i - 1]:
                continue
            if x - k in seen:
                ans += 1
            seen.add(x)
        return ans


"""
[3,1,4,1,5]
2
[1,2,3,4,5]
1
[1,3,1,5,4]
0
[1,2,4,4,3,3,0,9,2,3]
3
"""
