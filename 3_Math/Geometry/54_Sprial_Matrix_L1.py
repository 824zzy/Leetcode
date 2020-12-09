class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d, m, n = 0, len(A), len(A[0])
        ans = []
        visit = [[0 for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        for i in range(1, m*n+1):
            visit[x][y] = i
            ans.append(A[x][y])
            a, b = steps[d]
            if not (m>x+a>=0<=y+b<n and not visit[x+a][y+b]):
                d = (d+1)%4
                a, b = steps[d]
            x += a
            y += b
        return ans