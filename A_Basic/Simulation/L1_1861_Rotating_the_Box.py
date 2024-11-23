""" https://leetcode.com/problems/rotating-the-box/
string simulation
"""

from header import *


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i, row in enumerate(box):
            # count stones until obstacle
            r = 0
            while r < len(row):
                cnt = 0
                while r < len(row) and row[r] != "*":
                    if row[r] == "#":
                        cnt += 1
                    row[r] = "."
                    r += 1
                l = r
                for _ in range(cnt):
                    l -= 1
                    row[l] = "#"
                r += 1
            box[i] = row
        return zip(*box[::-1])


"""
[["#",".","#"]]
[["#",".","*","."],["#","#","*","."]]
[["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
"""
