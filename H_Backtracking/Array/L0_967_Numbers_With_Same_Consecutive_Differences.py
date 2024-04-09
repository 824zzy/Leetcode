""" https://leetcode.com/problems/numbers-with-same-consecutive-differences/
simple backtracking
"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        stk = []
        ans = []

        def dfs(i):
            if i == n:
                ans.append(int(''.join(map(str, stk.copy()))))
                return
            if stk[-1] + k < 10:
                stk.append(stk[-1] + k)
                dfs(i + 1)
                stk.pop()
            if k and stk[-1] - k >= 0:
                stk.append(stk[-1] - k)
                dfs(i + 1)
                stk.pop()

        for x in range(1, 10):
            stk.append(x)
            dfs(1)
            stk.pop()
        return ans
