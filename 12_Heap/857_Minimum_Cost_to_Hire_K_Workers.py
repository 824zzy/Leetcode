""" Greedy heap
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        H = []
        ans = float('inf')
        SUM = 0
        for r, q in workers:
            heapq.heappush(H, -q)
            SUM += q
            if len(H)>k: SUM += heapq.heappop(H)
            if len(H)==k: ans = min(ans, SUM*r)
        return ans