""" https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
Simulate game board
"""

from header import *


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        rows = [0] * N
        cols = [0] * N
        mainDiag = 0
        antiDiag = 0

        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                mainDiag += player
            if r + c == N - 1:
                antiDiag += player
            if (
                abs(rows[r]) == N
                or abs(cols[c]) == N
                or abs(mainDiag) == N
                or abs(antiDiag) == N
            ):
                return "A" if player == 1 else "B"
            player = -player

        return "Draw" if len(moves) == N * N else "Pending"
