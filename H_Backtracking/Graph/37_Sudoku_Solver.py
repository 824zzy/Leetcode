""" L1:
Find index trick: i, j = i-i%3, j-j%3
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, i, j, val):
            for x in range(9):
                if board[x][j] == val:
                    return False
            for y in range(9):
                if board[i][y] == val:
                    return False
            i, j = i - i % 3, j - j % 3
            for x in range(3):
                for y in range(3):
                    if board[x + i][y + j] == val:
                        return False
            return True

        def dfs(board, i, j):
            if i == 9:
                return True
            if j >= 9:
                return dfs(board, i + 1, 0)
            if board[i][j] != '.':
                return dfs(board, i, j + 1)
            for k in range(1, 10):
                if is_valid(board, i, j, str(k)):
                    board[i][j] = str(k)
                    if dfs(board, i, j):
                        return True
                    board[i][j] = '.'
            return False

        return dfs(board, 0, 0)
