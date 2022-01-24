""" https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/
perform dijkstra accurately and carefully
"""
class Solution:
    def highestRankedKItems(self, A: List[List[int]], P: List[int], start: List[int], k: int) -> List[List[int]]:
        x, y = start
        pq = [(0, A[x][y], x, y)]
        seen = set()
        seen.add((x, y))
        ans = []
        while pq:
            d1, p1, x, y = heapq.heappop(pq)
            if P[0]<=p1<=P[1]: 
                ans.append([x, y])
                if len(ans)==k: return ans
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and (x+dx, y+dy) not in seen and A[x+dx][y+dy]!=0:
                    seen.add((x+dx, y+dy))
                    heapq.heappush(pq, [d1+1, A[x+dx][y+dy], x+dx, y+dy])
        return ans