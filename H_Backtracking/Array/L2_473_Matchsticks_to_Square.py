""" https://leetcode.com/problems/matchsticks-to-square/
"""
# . fill matchsticks


class Solution:
    def makesquare(self, A: List[int]) -> bool:
        n = len(A)
        A.sort(reverse=True)
        k, rem = divmod(sum(A), 4)
        if rem or A[0] > k:
            return False

        seen = [0] * 15

        def dfs(i, group, sm):
            if group == 4:
                return True
            if sm > k:
                return False
            if sm == k:
                return dfs(0, group + 1, 0)

            for j in range(i, len(A)):
                if not seen[j]:
                    seen[j] = 1
                    if dfs(j + 1, group, sm + A[j]):
                        return True
                    seen[j] = 0
            return False

        return dfs(0, 0, 0)

# fill sides


class Solution:
    def makesquare(self, A: List[int]) -> bool:
        q, r = divmod(sum(A), 4)
        if len(A) < 4 or r:
            return False

        A.sort(reverse=True)
        sides = [0] * 4

        def dfs(k):
            """Return True if it is possible to make a square."""
            if k == len(A):
                return True
            seen = set()
            for i in range(4):
                sides[i] += A[k]
                if sides[i] <= q and sides[i] not in seen:
                    seen.add(sides[i])
                    if dfs(k + 1):
                        return True
                sides[i] -= A[k]
            return False

        return dfs(0)
