""" L0: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
No need to use seen and be careful to boundary conditions
"""
class Solution:
    def nearestExit(self, A: List[List[str]], E: List[int]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        Q = [E]
        ans = 0
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                A[x][y] = '+'
                if (x in [0, M-1] or y in [0, N-1]) and [x, y]!=E: return ans
                for dx, dy in D:
                    if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]=='.':
                        A[x+dx][y+dy] = '+'
                        Q.append([x+dx, y+dy])
            ans += 1
        return -1