""" L2: https://leetcode.com/problems/count-nodes-with-the-highest-score/
build a graph as a tree and consider 3 different cases for dfs
"""
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # build tree
        T = [[] for _ in range(len(parents))]
        for i, v in enumerate(parents):
            if v>=0: T[v].append(i)
        
        self.cnt = Counter()
        def dfs(node):
            if not T[node]: # no child
                l, r, p = 1, 1, len(T)-1
                self.cnt[l*r*p] += 1
                return 1
            elif len(T[node])==1: # 1 child
                c = dfs(T[node][0])
                p = len(T)-1-c or 1
                self.cnt[c*p] += 1
                return c+1
            else: # 2 children
                l, r = dfs(T[node][0]), dfs(T[node][1])
                p = len(T)-1-l-r or 1
                self.cnt[l*r*p] += 1
                return l+r+1
        
        dfs(0)
        return self.cnt[max(self.cnt)]