""" L2: TODO: convert to template format
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i==len(word):
                return True
            if r<0 or r>=len(board) or c<0 or c>=len(board[r]) or board[r][c]!=word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = ' '
            ans = dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1)
            board[r][c] = tmp
            return ans
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0] and dfs(i, j, 0):
                    return True
        return False