""" https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
prefix sum + two pointers

learn from guan: https://www.youtube.com/watch?v=7R10ZSepbS4&t=600s
"""


class Solution:
    def maximumWhiteTiles(self, A: List[List[int]], L: int) -> int:
        A.sort()
        prefix = list(accumulate([r - l + 1 for l, r in A]))

        j = 0
        ans = 0
        for i in range(len(A)):
            while j < len(A) and A[i][0] + L - 1 >= A[j][1]:
                j += 1
            cover = prefix[j - 1] - (prefix[i - 1] if i != 0 else 0)
            # add partial tiles at the end
            if j < len(A):
                cover += max(0, A[i][0] + L - 1 - A[j][0] + 1)
            ans = max(ans, cover)
        return ans
