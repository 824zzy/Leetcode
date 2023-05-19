""" https://leetcode.com/problems/most-popular-video-creator/
"""
from header import *

class Solution:
    def mostPopularCreator(self, C: List[str], ID: List[str], V: List[int]) -> List[List[str]]:
        creator2videos = defaultdict(list)
        creator2views = defaultdict(int)
        for c, i, v in zip(C, ID, V):
            creator2videos[c].append((-v, i))
            creator2views[c] += v
            
        ans = []
        mx = max(creator2views.values())
        for k, v in creator2views.items():
            if v==mx:
                ans.append([k, min(creator2videos[k])[1]])
        return ans
                    
"""
["alice","bob","alice","chris"]
["one","two","three","four"]
[5,10,5,4]
["alice","alice","alice"]
["a","b","c"]
[1,2,2]
"""
        