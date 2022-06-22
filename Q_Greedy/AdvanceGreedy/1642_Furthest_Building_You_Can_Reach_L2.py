""" https://leetcode.com/problems/furthest-building-you-can-reach/
let's suppose we have a minheap whose size is l and we always want to use ladders.
When we are run out of ladders, we need to use bricks to replace the ladders for the minimal height difference
"""
# remove ladder first
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

# remove bricks first
class Solution:
    def furthestBuilding(self, A: List[int], b: int, l: int) -> int:
        pq = []
        for i in range(len(A)-1):
            d = A[i+1]-A[i]
            if d>0:
                heappush(pq, -d)
                b -= d
                if b<0:
                    if l==0: return i
                    b -= heappop(pq)
                    l -= 1
        return len(A)-1