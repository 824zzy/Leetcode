""" L1
Simulate by directions.
"""
class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        ans = []
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        for i in range(len(A)*len(A[0])):
            ans.append(A[x][y])
            A[x][y] = float('inf')
            dx, dy = D[d]
            if not (0<=x+dx<len(A) and 0<=y+dy<len(A[0])) or A[x+dx][y+dy]==float('inf'):
                d = (d+1)%4
                dx, dy = D[d]
            x += dx
            y += dy
        return ans