""" L1
Since we have k stop limit, seen dict is not necessary.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        e = collections.defaultdict(dict)
        for i, j, p in flights: e[i][j] = p
        pq = [(0, src, k+1)]
        while pq:
            p, i, k = heapq.heappop(pq)
            if i==dst: return p
            if k>0:
                for j in e[i]:
                    heapq.heappush(pq, (p+e[i][j], j, k-1))
        return -1