""" https://leetcode.com/problems/path-with-minimum-effort/
use dijkstra's algorithm to find the shortest path in a weighted graph whose weight is the maximum absolute difference.

Time: O(ElogV), where E=4*M*N and V=M*N
"""
class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = defaultdict(lambda: inf)
        seen[(0, 0)] = 0
        
        while pq:
            e1, x, y = heappop(pq)
            if x==len(A)-1 and y==len(A[0])-1: return e1
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                    e2 = abs(A[x+dx][y+dy]-A[x][y])
                    e = max(e1, e2)
                    if e<seen[(x+dx, y+dy)]:
                        seen[(x+dx, y+dy)] = e
                        heappush(pq, (e, x+dx, y+dy))