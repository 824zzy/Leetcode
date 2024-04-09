""" https://leetcode.com/problems/find-pivot-index/
1. compute prefix and suffix sum
2. linear scan and find the index where prefix[i]==suffix[i-1]
"""


class Solution:
    def pivotIndex(self, A: List[int]) -> int:
        prefix = list(accumulate(A, initial=0))
        suffix = list(accumulate(A[::-1], initial=0))[::-1]

        for i in range(len(prefix)):
            if i and prefix[i] == suffix[i - 1]:
                return i - 1
        return -1
