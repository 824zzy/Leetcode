""" https://leetcode.com/problems/subsets/
find all subsets by dfs(P+[n], N[i+1:])
"""


class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        stk = []

        def dfs(i):
            ans.append(stk.copy())
            if i == len(A):
                return
            for j in range(i, len(A)):
                stk.append(A[j])
                dfs(j + 1)
                stk.pop()

        dfs(0)
        return ans


# dfs with state


class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        self.ans = []

        def dfs(P, N):
            self.ans.append(P)
            if not N:
                return
            for i, n in enumerate(N):
                dfs(P + [n], N[i + 1 :])

        dfs([], A)
        return self.ans
