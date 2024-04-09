""" https://leetcode.com/problems/minesweeper/
a complex simulation
"""
from header import *


class Solution:
    def updateBoard(self, B: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        cx, cy = click
        # case 1
        if B[cx][cy] == 'M':
            B[cx][cy] = 'X'
            return B
        # use a copy to find digits around mines
        _B = deepcopy(B)
        M = [(i, j) for i in range(len(_B))
             for j in range(len(_B[0])) if _B[i][j] == "M"]
        for x, y in M:
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -
                                                    1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                if 0 <= x + dx < len(B) and 0 <= y + dy < len(B[0]):
                    if _B[x + dx][y + dy] == "E":
                        _B[x + dx][y + dy] = 1
                    elif isinstance(_B[x + dx][y + dy], int):
                        _B[x + dx][y + dy] += 1
        # bfs to populate matrix
        Q = [(cx, cy)]
        seen = set(Q)
        if _B[cx][cy] == 'E':
            B[cx][cy] = 'B'
        elif isinstance(_B[cx][cy], int):
            B[cx][cy] = str(_B[cx][cy])
            return B

        while Q:
            nxtQ = []
            for x, y in Q:
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -
                                                        1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                    if (x + dx, y + dy) not in seen:
                        seen.add((x + dx, y + dy))
                        if 0 <= x + dx < len(B) and 0 <= y + dy < len(B[0]):
                            if _B[x + dx][y + dy] == 'E':
                                B[x + dx][y + dy] = 'B'
                                nxtQ.append((x + dx, y + dy))
                            elif isinstance(_B[x + dx][y + dy], int):
                                B[x + dx][y + dy] = str(_B[x + dx][y + dy])
            Q = nxtQ
        return B


"""
[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
[3,0]
[["E","E","E","E","E"],["E","M","M","M","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
[3,0]
[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
[1,2]
[["E","M","M","2","B","B","B","B"],["E","E","M","2","B","B","B","B"],["E","E","2","1","B","B","B","B"],["E","M","1","B","B","B","B","B"],["1","2","2","1","B","B","B","B"],["B","1","M","1","B","B","B","B"],["B","1","1","1","B","B","B","B"],["B","B","B","B","B","B","B","B"]]
[0,0]
"""
