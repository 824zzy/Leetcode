""" https://leetcode.com/problems/combination-sum-ii/
use backtracking to find distinct combination sum and (i==j or A[j-1]!=A[j]) statement to filter out duplicates
"""


class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        if sum(A) < target:
            return []
        stk = []
        ans = []
        A.sort()

        def dfs(i, t):
            if t == 0:
                return ans.append(stk.copy())
            for j in range(i, len(A)):
                if t - A[j] >= 0 and (i == j or A[j - 1] != A[j]):
                    stk.append(A[j])
                    dfs(j + 1, t - A[j])
                    stk.pop()

        dfs(0, target)
        return ans
