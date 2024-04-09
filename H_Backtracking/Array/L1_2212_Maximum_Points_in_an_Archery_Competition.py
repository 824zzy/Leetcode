""" https://leetcode.com/problems/maximum-points-in-an-archery-competition/
Essentially a knap sack problem which use back tracking to obtain Bob's scoring section
"""


class Solution:
    def maximumBobPoints(self, n: int, A: List[int]) -> List[int]:
        self.ans = []
        stk = []
        self.maxS = -inf

        @cache
        def dfs(i, n, score):
            if i == len(A):
                if score > self.maxS:
                    self.ans, self.maxS = stk.copy(), score
                return
            # Bob wins this section
            if n - A[i] - 1 >= 0:
                stk.append(A[i] + 1)
                dfs(i + 1, n - A[i] - 1, score + i)
                stk.pop()
            # Bob losses this section
            stk.append(0)
            dfs(i + 1, n, score)
            stk.pop()

        dfs(0, n, 0)
        # add remained arrows for Bob
        if sum(self.ans) != n:
            self.ans[0] += n - sum(self.ans)
        return self.ans
