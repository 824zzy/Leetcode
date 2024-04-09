""" https://leetcode.com/problems/n-queens/
1. create the board "A" for simulation
2. create hash table "seen" whose keys are column, left diagonal, right diagonal and values are visited indexes
3. use backtracking to find valid answers
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        A = [['.' for _ in range(n)] for _ in range(n)]
        seen = defaultdict(list)
        ans = []

        def dfs(i):
            if i == n:
                return ans.append([''.join(r) for r in A])
            for j in range(n):
                if j not in seen['col'] and i + \
                        j not in seen['ldiag'] and i - j not in seen['rdiag']:
                    A[i][j] = 'Q'
                    seen['col'].append(j)
                    seen['ldiag'].append(i + j)
                    seen['rdiag'].append(i - j)
                    dfs(i + 1)
                    A[i][j] = '.'
                    seen['col'].pop()
                    seen['ldiag'].pop()
                    seen['rdiag'].pop()

        dfs(0)
        return ans
