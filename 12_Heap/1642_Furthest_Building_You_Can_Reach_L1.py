""" https://leetcode.com/problems/furthest-building-you-can-reach/
"""
class Solution:
    def furthestBuilding(self, A: List[int], b: int, l: int) -> int:
        H = []
        for i in range(len(A)-1):
            d = A[i+1]-A[i]
            if d>0:
                heapq.heappush(H, d)
                if len(H)>l:
                    b -= heapq.heappop(H)
                    if b<0: return i
        
        return len(A)-1