# neat solution
from collections import defaultdict
class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for items, val in zip(e, v):
            x, y = items
            g[x].add((y, val))
            g[y].add((y, 1.0/val))
        
        def dfs(n0, n1):
            if n0==n1 and graph[n0]:
                return 1
            visit.add(n0)
            for neigh, val in graph[start]:
                if neigh not in visit:
                    tmp = dfs(n1, neigh)
                    if tmp>0:
                        return val*tmp
            return -1
            
        ans = []
        for q in queries:
            graph = g.copy()
            visit = set()
            res.append(dfs(q[0], q[1]))
            
            
# naive solutoin
from collections import defaultdict
class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], q: List[List[str]]) -> List[float]:
        if not e:
            return 0
        n = len(e)
        g = defaultdict(list)
        for i in range(n):
            g[e[i][0]].append(e[i][1])
            g[e[i][1]].append(e[i][0])
            g[e[i][0]].append(e[i][0])
            g[e[i][1]].append(e[i][1])

        def dfs(node, target, path):
            if node==target:
                self.path = path
                return
            
            for n in g[node]:
                if not visit[n]:
                    visit[n] = 1
                    dfs(n, target, path+[(node, n)])
        
        nodes = {}
        for c in e:
            nodes[c[0]] = 0
            nodes[c[1]] = 0
        
        factor = {}
        for i, eq in enumerate(e):
            factor[tuple(eq)] = v[i]
            factor[tuple(reversed(eq))] = 1/v[i]
            factor[tuple([eq[0], eq[0]])] = 1
            factor[tuple([eq[1], eq[1]])] = 1
        
        ans = []
        for i in q:
            if i[0]==i[1] and (i[0], i[1]) in factor:
                ans.append(factor[(i[0], i[1])])
            else:
                visit = nodes.copy()
                self.path = []
                dfs(i[0], i[1], [])
                res = 1
                if not self.path:
                    ans.append(-1)
                else:
                    for p in self.path:
                        res *= factor[p]
                    ans.append(res)
        return ans