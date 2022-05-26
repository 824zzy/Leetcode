""" https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
1. use dfs to iterate on all the nodes
2. the 2 longest path can make up the longest path in subtree of node
"""
class Solution:
    def longestPath(self, P: List[int], s: str) -> int:
        G = defaultdict(list)
        for i, j in enumerate(P):
            if j>=0: G[j].append(i)
        
        self.ans = 0
        
        def dfs(i):
            cand = [0]
            for j in G[i]:
                tmp = dfs(j)
                if s[i]!=s[j]:
                    cand.append(tmp)
                    
            cand = nlargest(2, cand)
            self.ans = max(self.ans, sum(cand)+1)
            return max(cand)+1
        
        dfs(0)    
        return self.ans