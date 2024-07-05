""" https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
brute force simulation
"""
from header import *

# optimized by hash table: O(M*N)


class Solution:
    def differenceOfDistinctValues(self, G: List[List[int]]) -> List[List[int]]:
        M, N = len(G), len(G[0])
        tl = defaultdict(set)
        br = defaultdict(set)
        for i in range(M):
            for j in range(N):
                pre = tl[(i - 1, j - 1)].copy()
                pre.add(G[i][j])
                tl[(i, j)] = pre

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                pre = br[(i + 1, j + 1)].copy()
                pre.add(G[i][j])
                br[(i, j)] = pre

        ans = [[0 for j in range(N)] for i in range(M)]
        for i in range(M):
            for j in range(N):
                ans[i][j] = abs(len(tl[(i - 1, j - 1)]) - len(br[(i + 1, j + 1)]))
        return ans


# brute force: O(M*N*min(M, N))


class Solution:
    def differenceOfDistinctValues(self, G: List[List[int]]) -> List[List[int]]:
        M, N = len(G), len(G[0])
        ans = [[0 for j in range(N)] for i in range(M)]
        for i in range(M):
            for j in range(N):
                x, y = i - 1, j - 1
                tl = set()
                while 0 <= x and 0 <= y:
                    tl.add(G[x][y])
                    x -= 1
                    y -= 1
                x, y = i + 1, j + 1
                br = set()
                while x < M and y < N:
                    br.add(G[x][y])
                    x += 1
                    y += 1
                ans[i][j] = abs(len(tl) - len(br))
        return ans
