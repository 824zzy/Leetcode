""" https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
we can remove i + 1 elements from front,
or we can remove n - i elements from back.
"""


class Solution:
    def minimumDeletions(self, A):
        i, j, n = A.index(min(A)), A.index(max(A)), len(A)
        return min(max(i + 1, j + 1), max(n - i, n - j),
                   i + 1 + n - j, j + 1 + n - i)
