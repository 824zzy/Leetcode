""" https://leetcode.com/problems/number-of-paths-with-max-score/
top down dp while keeping track of path count
"""


class Solution:
    def pathsWithMaxScore(self, A: List[str]) -> List[int]:
        @cache
        def dfs(i, j):
            if i == 0 and j == 0:
                return 0, 1
            elif not (0 <= i < len(A) and 0 <= j < len(A[0])) or A[i][j] == 'X':
                return -inf, 0

            val = int(A[i][j]) if A[i][j] != 'S' else 0
            cnt = 0

            s1, c1 = dfs(i - 1, j)
            s2, c2 = dfs(i - 1, j - 1)
            s3, c3 = dfs(i, j - 1)

            maxS = max([s1, s2, s3])
            if s1 == maxS:
                cnt += c1
            if s2 == maxS:
                cnt += c2
            if s3 == maxS:
                cnt += c3

            return val + maxS, cnt

        s, c = dfs(len(A) - 1, len(A[0]) - 1)
        return s % (10**9 + 7) if s != -inf else 0, c % (10**9 + 7)
