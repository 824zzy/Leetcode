""" https://leetcode.com/problems/sum-of-all-subset-xor-totals/
find all subset by dfs(P^n, N[i+1:])
"""
# backtracking


class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        def dfs(i):
            ans.append(self.stk)
            if i == len(A):
                return
            for j in range(i, len(A)):
                self.stk ^= A[j]
                dfs(j + 1)
                self.stk ^= A[j]

        ans = []
        self.stk = 0
        dfs(0)
        return sum(ans)

# dfs with states


class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        self.ans = 0

        def dfs(P, N):
            self.ans += P
            if not N:
                return
            for i, n in enumerate(N):
                dfs(P ^ n, N[i + 1:])

        dfs(0, A)
        return self.ans
