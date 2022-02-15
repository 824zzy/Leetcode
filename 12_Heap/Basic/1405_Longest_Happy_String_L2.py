""" https://leetcode.com/problems/longest-happy-string/
greedily pop max heap
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [] # max-heap 
        for x, c in zip((a, b, c), "abc"): 
            if x: heappush(pq, (-x, c))
        
        ans = []
        while pq: 
            n, x = heappop(pq)
            if ans[-2:] != [x, x]: 
                ans.append(x)
                if n+1: heappush(pq, (n+1, x))
            else: 
                if not pq: break 
                nn, xx = heappop(pq)
                ans.append(xx)
                if nn+1: heappush(pq, (nn+1, xx))
                heappush(pq, (n, x))
        return "".join(ans)