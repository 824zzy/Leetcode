""" https://leetcode.com/problems/design-tic-tac-toe/
1. keep track of rows, cols, and diagonals count of each player
2. once a player has a count of n, return the player
"""


class TicTacToe:
    def __init__(self, n: int):
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.dig = [0, 0]
        self.rev_dig = [0, 0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        p = player - 1
        self.rows[row][p] += 1
        self.cols[col][p] += 1
        if row == col:
            self.dig[p] += 1
        if row + col == self.n - 1:
            self.rev_dig[p] += 1
        if any(
            x == self.n
            for x in (
                self.rows[row][p],
                self.cols[col][p],
                self.dig[p],
                self.rev_dig[p],
            )
        ):
            return player
        return 0


"""
["TicTacToe","move","move","move","move","move","move","move"]
[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
["TicTacToe","move","move","move"]
[[2],[0,0,2],[0,1,1],[1,1,2]]
"""
