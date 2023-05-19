""" https://leetcode.com/problems/longest-happy-string
The same as 984

"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        for x, ch in [[-a, 'a'], [-b, 'b'], [-c, 'c']]: 
            if x: pq.append([x, ch])
        heapify(pq)
        ans = ''
        
        while pq:
            if len(pq)==1: 
                ans += min(-pq[0][0], 2)*pq[0][1]
                return ans
            
            x, chx = heappop(pq)
            y, chy = heappop(pq)
            # stride can be just 1 or 2
            k = min(-(x-y)+1, 2)
            for _ in range(k): ans += chx
            ans += chy
            
            if x+k<0: heappush(pq, [x+k, chx])
            if y+1<0: heappush(pq, [y+1, chy])
        return ans