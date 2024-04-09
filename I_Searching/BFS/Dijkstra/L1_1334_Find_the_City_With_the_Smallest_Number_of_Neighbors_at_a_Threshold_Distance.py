""" https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Use dijkstra algorithm to find the shortest path from each point to the others.
"""
from header import *


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], T: int) -> int:
        e = defaultdict(dict)
        for i, j, k in edges:
            e[i][j] = k
            e[j][i] = k

        ans = (float('inf'), float('-inf'))
        for start in range(n):
            pq = [(-T, start)]
            seen = Counter()
            while pq:
                t1, i = heapq.heappop(pq)
                if i not in seen:
                    seen[i] = 1
                    for j in e[i]:
                        t2 = t1 + e[i][j]
                        if j not in seen and t2 <= 0:
                            heapq.heappush(pq, (t2, j))
            cnt = sum(seen.values()) - 1
            if (cnt == ans[0] and start > ans[1]) or (cnt < ans[0]):
                ans = (cnt, start)
        return ans[1]
