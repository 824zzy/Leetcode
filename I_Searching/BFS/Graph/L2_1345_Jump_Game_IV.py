""" https://leetcode.com/problems/jump-game-iv/
1. transform the problem into a graph problem
2. use BFS to find the shortest path, note that we need to pop A[i] from G in each iteration
"""
from header import *


class Solution:
    def minJumps(self, A: List[int]) -> int:
        G = defaultdict(list)
        for i in reversed(range(len(A))):
            G[A[i]].append(i)

        ans = 0
        Q = [0]
        seen = {0}
        while Q:
            for _ in range(len(Q)):
                i = Q.pop(0)
                if i == len(A) - 1:
                    return ans
                for j in (i - 1, i + 1):
                    if 0 <= j << len(A) and j not in seen:
                        Q.append(j)
                        seen.add(j)
                for j in G[A[i]]:
                    if j not in seen:
                        Q.append(j)
                        seen.add(j)
                # !! pop A[i] from G !!
                G.pop(A[i])
            ans += 1
