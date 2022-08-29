""" https://leetcode.com/problems/count-nodes-with-the-highest-score/
Observation: f(x) = left_subtree_size * right_subtree_size * (n-left_subtree_size-right_subtree_size-1)
use dfs to calculate score based on the above formula
"""
from header import *

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        G = defaultdict(list)
        for i, x in enumerate(parents):
            if i==0: continue
            G[x].append(i)
        
        ans = Counter()
        def dfs(i):
            score = 1
            cnt = 0
            for j in G[i]:
                subtree_size = dfs(j)
                score *= subtree_size
                cnt += subtree_size
            score *= max(n-cnt-1, 1)
            ans[score] += 1
            return cnt+1
        
        dfs(0)
        return ans[max(ans)]
            
                
"""
[-1,2,0,2,0]
[-1,2,0]
[-1,3,3,5,7,6,0,0]
"""