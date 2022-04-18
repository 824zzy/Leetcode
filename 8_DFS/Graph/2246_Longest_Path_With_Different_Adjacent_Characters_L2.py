""" https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
learn from lee: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/discuss/1955433/JavaC%2B%2BPython-DFS-on-Tree
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
            ans = [0, 0]
            for j in G[i]:
                tmp = dfs(j)
                if s[i]!=s[j]:
                    ans.append(tmp)
                    
            ans = nlargest(2, ans)
            self.ans = max(self.ans, ans[0]+ans[1]+1)
            return max(ans)+1
        
        dfs(0)    
        return self.ans