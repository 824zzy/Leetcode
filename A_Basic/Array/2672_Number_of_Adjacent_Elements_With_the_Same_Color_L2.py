""" https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/
Each time you make a change, it only affects the relationship between the current element and its adjacent ones, so you can just simulate it.
"""
from header import *

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        mp = defaultdict(int)
        cnt = 0
        ans = []
        for i, c in queries:
            if mp[i]:
                if i+1<n and mp[i+1]==mp[i]:
                    cnt -= 1
                if i>0 and mp[i-1]==mp[i]:
                    cnt -= 1
            mp[i] = c
            if i+1<n and mp[i+1]==mp[i]:
                cnt += 1
            if i>0 and mp[i-1]==mp[i]:
                cnt += 1
            ans.append(cnt)
        return ans
                
        
"""
11111 : 4
11211 : 2
"""