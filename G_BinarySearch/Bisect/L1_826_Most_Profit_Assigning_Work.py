""" https://leetcode.com/problems/most-profit-assigning-work/
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        A = sorted(zip(difficulty, profit))
        _A = []
        for i, (k, x) in enumerate(A):
            if not _A or x > _A[-1][1]:
                _A.append([k, x])
        A = _A

        ans = 0
        for w in worker:
            i = bisect_right(A, [w, inf]) - 1
            if i != -1:
                ans += A[i][1]
        return ans
