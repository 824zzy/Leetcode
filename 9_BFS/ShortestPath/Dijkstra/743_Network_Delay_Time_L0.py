""" https://leetcode.com/problems/network-delay-time/
use dijkstra to find minimum delay for all the nodes to receive the signal
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        e = collections.defaultdict(dict)
        for i, j, d in times: e[i][j] = d
        pq = [(0, k)]
        seen = {}
        while pq:
            delay, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = delay
                for j in e[i]:
                    delay2 = delay+e[i][j]
                    if j not in seen:
                        heapq.heappush(pq, (delay2, j))
        if len(seen)!=n: return -1
        else: return max(seen.values())