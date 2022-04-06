""" https://leetcode.com/problems/n-queens/
1. create the board "A" for simulation
2. create hash table "seen" whose keys are column, left diagonal, right diagonal and values are visited indexes
3. use backtracking to find valid answers
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        A = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        
        def dfs(i, seen):
            if i==n: return ans.append(["".join(r) for r in A])
            for j in range(n):
                if j not in seen['col'] and i+j not in seen['ldiag'] and i-j not in seen['rdiag']:
                    A[i][j] = 'Q'
                    seen['col'].add(j)
                    seen['ldiag'].add(i+j)
                    seen['rdiag'].add(i-j)
                    dfs(i+1, seen)
                    A[i][j] = '.'
                    seen['col'].remove(j)
                    seen['ldiag'].remove(i+j)
                    seen['rdiag'].remove(i-j)

        seen = defaultdict(set)
        dfs(0, seen)
        return ans


# elegent solution from ye15: https://leetcode.com/problems/n-queens/discuss/668701/Python3-backtracking
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        
        def fn(i, seen): 
            """Recursively populate the n queens via backtracking."""
            if i == n: return ans.append(["".join(x) for x in board])
            for j in range(n): 
                pos = {("col", j), ("diag", i-j), ("anti", i+j)}
                if not pos & seen: 
                    board[i][j] = "Q"
                    seen |= pos
                    fn(i+1, seen)
                    board[i][j] = "."
                    seen -= pos
        
        ans = []
        fn(0, set())
        return ans