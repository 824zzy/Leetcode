"""L2: Monotonic priority queue
TODO: create a template for this type of problem, similar to monotonic stack
"""
class Solution:
    def minRefuelStops(self, t: int, cur: int, S: List[List[int]]) -> int:
        pq = []
        ans = i = 0
        while cur<t:
            while i<len(S) and S[i][0]<=cur:
                heapq.heappush(pq, -S[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            ans += 1
        return ans