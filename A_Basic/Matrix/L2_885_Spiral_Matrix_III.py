""" https://leetcode.com/problems/spiral-matrix-iii/
learn from lee: https://leetcode.com/problems/spiral-matrix-iii/discuss/158970/C%2B%2BJavaPython-112233-Steps
generate sequence whose length of each side is following: 1,1,2,2,3,3,4,4, ....
"""


class Solution:
    def spiralMatrixIII(self, r: int, c: int, x: int,
                        y: int) -> List[List[int]]:
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        dx, dy = D[d]
        n = 0

        ans = []
        while len(ans) < r * c:
            for _ in range(n // 2 + 1):
                if 0 <= x < r and 0 <= y < c:
                    ans.append([x, y])
                x, y = x + dx, y + dy
            d = (d + 1) % 4
            dx, dy = D[d]
            n += 1
        return ans
