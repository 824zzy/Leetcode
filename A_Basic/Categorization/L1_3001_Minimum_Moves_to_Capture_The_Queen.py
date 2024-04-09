""" https://leetcode.com/problems/minimum-moves-to-capture-the-queen/
categorization
"""


class Solution:
    def minMovesToCaptureTheQueen(
        self,
        a: int,
        b: int,
        c: int,
        d: int,
        e: int,
            f: int) -> int:
        R, B, Q = (a, b), (c, d), (e, f)
        ans = 2
        # Queen can be captured by Rook in 1 move
        if (R[0] == Q[0] and not (R[0] == B[0] and (R[1] < B[1] < Q[1] or Q[1] < B[1] < R[1]))) or (
                R[1] == Q[1] and not (R[1] == B[1] and (R[0] < B[0] < Q[0] or Q[0] < B[0] < R[0]))):
            ans = 1
        # Queen can be captured by Bishops in 1 move
        # diagonal
        if B[0] - Q[0] == B[1] - Q[1]:
            if not (
                B[0] -
                R[0] == B[1] -
                R[1] and (
                    Q[0] < R[0] < B[0] or B[0] < R[0] < Q[0])):
                ans = 1
        # anti-diagonal
        if B[0] - Q[0] == Q[1] - B[1]:
            if not (
                B[0] -
                R[0] == R[1] -
                B[1] and (
                    Q[0] < R[0] < B[0] or B[0] < R[0] < Q[0])):
                ans = 1
        return ans


"""
1
1
8
8
2
3
5
3
3
4
5
2
4
3
3
4
2
5
1
1
8
2
4
1
1
6
3
3
5
6
3
7
1
5
3
2
"""
