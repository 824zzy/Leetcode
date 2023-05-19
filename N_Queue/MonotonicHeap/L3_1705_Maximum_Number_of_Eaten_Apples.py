""" L2: https://leetcode.com/problems/maximum-number-of-eaten-apples/
"""
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        
        pq = []
        for i, (x, d) in enumerate(zip(apples, days)):
            while pq and pq[0][0]<=i: heappop(pq) # rotten
            if x: heappush(pq, (i+d, x)) # new apples
            if pq:
                ii, x = heappop(pq)
                if x-1: heappush(pq, (ii, x-1))
                ans += 1
                
        i += 1
        while pq:
            ii, x = heappop(pq)
            x = min(x, ii-i)
            ans += x
            i += x
        return ans