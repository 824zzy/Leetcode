""" https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
group string and check if the maximal length segment is 1
Time: O(N) Space: O(N)
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        A = [[int(k), len(list(v))] for k, v in groupby(s)]
        x = max(A, key=lambda x: (x[1], -x[0]))
        return x[0] == 1
