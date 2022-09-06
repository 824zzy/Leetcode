""" https://leetcode.com/problems/meeting-rooms-iii/
"""
from header import *
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        A = [(0, i, 0) for i in range(n)]
        for i, j in meetings:
            for idx, (ii, x, cnt) in enumerate(A):
                if ii<=i: A[idx] = (0, x, cnt)
            heapify(A)
            ii, x, cnt = heappop(A)
            if ii<=i:
                heappush(A, (j, x, cnt+1))
            else:
                heappush(A, (ii+(j-i), x, cnt+1))
        A.sort(key=lambda x: (-x[2], x[1]))
        return A[0][1]
    
""" 0 1 0 0 0
2
[[0,10],[1,5],[2,7],[3,4]]
3
[[1,20],[2,10],[3,5],[4,9],[6,8]]
4
[[18,19],[3,12],[17,19],[2,13],[7,10]]
4
[[10,11],[13,15],[9,19],[0,12],[12,20]]
5
[[40,47],[7,16],[27,38],[16,43],[38,40],[2,25]]
"""