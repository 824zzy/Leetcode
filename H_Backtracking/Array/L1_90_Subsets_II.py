""" https://leetcode.com/problems/subsets-ii/
"""
# optimized backtracking


class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        stk = []

        def dfs(i):
            if i == len(A):
                return ans.append(stk.copy())
            if not stk or A[i] != stk[-1]:
                dfs(i + 1)
            stk.append(A[i])
            dfs(i + 1)
            stk.pop()

        dfs(0)
        return ans


# backtracking


class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        stk = []

        def dfs(i):
            if stk not in ans:
                ans.append(stk.copy())
            if i == len(A):
                return
            for j in range(i, len(A)):
                stk.append(A[j])
                dfs(j + 1)
                stk.pop()

        dfs(0)
        return ans
