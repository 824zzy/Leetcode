""" L2: https://leetcode.com/problems/second-minimum-time-to-reach-destination/
dijkstra + math
predefine seen to avoid circle.
https://leetcode.com/problems/second-minimum-time-to-reach-destination/discuss/1525227/Python3-Dijkstra-ish
"""
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], T: int, C: int) -> int:
        e = defaultdict(dict)
        for i, j in edges:
            e[i-1][j-1] = T
            e[j-1][i-1] = T
        
        Q = [(0, 0)]
        seen = [[inf, inf] for _ in range(n)]
        least = None
        while Q:
            for _ in range(len(Q)):
                t, i = heapq.heappop(Q)
                if i==n-1:
                    if least is None: least = t
                    elif least<t: return t
                if (t//C) & 1: t = (t//C+1)*C
                t += T
                for j in e[i]:
                    if t!=seen[j][0] and t<seen[j][1]:
                        if t<seen[j][0]: seen[j] = [t, seen[j][0]]
                        else: seen[j][1] = t
                        heapq.heappush(Q, (t, j))