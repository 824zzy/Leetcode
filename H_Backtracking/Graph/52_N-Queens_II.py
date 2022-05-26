""" L2: The same as 51
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, n):
            if row==n: 
                ans.append(["".join(r) for r in B])
                return
            for i in range(n):
                if col[i] or ldiag[n-row+i-1] or rdiag[row+i]:
                    continue
                B[row][i] = 'Q'
                col[i] = ldiag[n-row+i-1] = rdiag[row+i] = 1
                dfs(row+1, n)
                B[row][i] = '.'
                col[i] = ldiag[n-row+i-1] = rdiag[row+i] = 0

        ans = []
        if n==0: return ans
        B = [["." for _ in range(n)] for _ in range(n)]
        col = [0] * n
        ldiag = [0] * (2*n-1)
        rdiag = [0] * (2*n-1)
        dfs(0, n)
        return len(ans)