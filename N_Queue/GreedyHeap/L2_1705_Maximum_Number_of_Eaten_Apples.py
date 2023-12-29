""" https://leetcode.com/problems/maximum-number-of-eaten-apples/
1. greedily eat the apples will be rotten soon ==> use priory queue to store apples
2. calculate the answer in two stages:
    1. within len(A) days
    2. the apples remained in queue
"""
from header import *

class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        pq = []
        ans = 0
        for t, (a, d) in enumerate(zip(A, D)):
            # out:the rotten apple
            while pq and pq[0][0]<=t:
                heappop(pq)
            # in: new apples
            if a:
                heappush(pq, [t+d, a])
            # update answer
            if pq:
                pq[0][1] -= 1
                if pq[0][1]==0:
                    heappop(pq)
                ans += 1
        t += 1
        while pq:
            while pq and pq[0][0]<=t:
                heappop(pq)
            if len(pq)==0:
                break
            d, a = heappop(pq)
            can_eat = min(a, d-t)
            t += can_eat
            ans += can_eat
        return ans
        
"""
[1,2,3,5,2]
[3,2,1,4,2]
[3,0,0,0,0,2]
[3,0,0,0,0,2]
"""