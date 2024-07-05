""" https://leetcode.com/problems/minimum-time-to-finish-the-race/
precompute the optimal tires of continuously using the same tire,
note that the upper bound of single lap time is 19, since changeTime<=100000 and r>=2, then 1*2^x<=100000 => x<17
then use dp to find minimum time to finish the race
"""


class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        tires = list(set([tuple(x) for x in tires]))
        A = [[0 for _ in range(len(tires))] for _ in range(17)]

        for i in range(17):
            for j, (f, r) in enumerate(tires):
                if i:
                    A[i][j] = A[i - 1][j] + f * r ** i
                else:
                    A[i][j] = f * r ** i

        A = [min(x) for x in A]

        @cache
        def dp(L):
            if L <= 0:
                return -changeTime
            ans = inf
            for i, x in enumerate(A):
                ans = min(ans, x + dp(L - i - 1) + changeTime)
            return ans

        return dp(numLaps)
