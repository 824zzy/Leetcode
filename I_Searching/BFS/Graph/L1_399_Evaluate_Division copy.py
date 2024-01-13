""" https://leetcode.com/problems/evaluate-division/
not very easy to notice it is a graph problem
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = defaultdict(dict)
        for idx, (i, j) in enumerate(equations):
            G[i][j] = values[idx]
            G[j][i] = 1/values[idx]
            
        def bfs(s, e):
            Q = [[s, 1]]
            seen = set([s])
            while Q:
                i, v = Q.pop(0)
                if i==e: return v
                for j in G[i]:
                    if j not in seen:
                        Q.append([j, v*G[i][j]])
                        seen.add(j)
            else: return -1
            
        
        ans = []
        for s, e in queries:
            if s in G and e in G: ans.append(bfs(s, e))
            else: ans.append(-1)
        return ans