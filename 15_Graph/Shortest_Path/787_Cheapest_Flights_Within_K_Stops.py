""" L2
"""
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, 0)]
        seen = {}
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst and K>=k-1: return p
            if i not in seen or seen[i]>k:
                seen[i] = k
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k+1))
        return -1