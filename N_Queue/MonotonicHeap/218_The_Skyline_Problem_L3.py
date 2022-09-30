""" https://leetcode.com/problems/the-skyline-problem/
https://leetcode.com/problems/the-skyline-problem/discuss/741467/Python3-priority-queue
"""
from header import *

class Solution:
    def getSkyline(self, A: List[List[int]]) -> List[List[int]]:
        A.append([inf, inf, 0]) # sentinel 
        
        ans, pq = [], [] # max-heap 
        for li, ri, hi in A: 
            while pq and -pq[0][1] < li: 
                _, rj = heappop(pq) 
                while pq and -pq[0][1] <= -rj: heappop(pq) 
                hj = pq[0][0] if pq else 0
                ans.append((-rj, -hj))
            if 0 < hi and (not pq or -pq[0][0] < hi): 
                if ans and ans[-1][0] == li: ans.pop()
                ans.append((li, hi))
            heappush(pq, (-hi, -ri))
        return ans 