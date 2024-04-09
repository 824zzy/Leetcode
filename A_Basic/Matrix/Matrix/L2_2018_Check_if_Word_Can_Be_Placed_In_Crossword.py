""" https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
not easy to brute force
"""


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        for x in board, zip(*board):
            for row in x:
                for s in "".join(row).split("#"):
                    for w in word, word[::-1]:
                        if len(s) == len(w) and all(ss in (" ", ww)
                                                    for ss, ww in zip(s, w)):
                            return True
        return False
