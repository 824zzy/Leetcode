""" https://leetcode.com/problems/subsets/
Use bit to indicate which element should be included
"""
# iterative


class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        for mask in range(1 << len(A)):
            # or mask & 1<<i
            ans.append([A[i] for i in range(len(A)) if mask >> i & 1])
        return ans


# recursive
class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        N = len(A)

        @cache
        def dp(mask):
            ans.append([A[i] for i in range(N) if mask & (1 << i)])
            if mask == (1 << N) - 1:
                return
            for i in range(N):
                if not mask & (1 << i):
                    dp(mask ^ (1 << i))

        dp(0)
        return ans
