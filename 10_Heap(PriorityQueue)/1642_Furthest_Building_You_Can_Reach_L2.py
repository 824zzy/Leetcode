"""
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        H = []
        for i in range(1, len(heights)):
            d = heights[i]-heights[i-1]
            if d<=0: continue
            heapq.heappush(H, d)
            if len(H)<=ladders: continue
            bricks -= heapq.heappop(H)
            if bricks<0: return i-1
        return len(heights)-1