""" https://leetcode.com/problems/count-the-number-of-complete-components/
complete component's property: v*(v-1)/2==e
"""
from header import *

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:        
        G = [[] for _ in range(n)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        
        def dfs(i):
            seen.add(i)
            v[0] += 1
            # will count edges twice
            e[0] += len(G[i])
            for j in G[i]:
                if j not in seen:
                    dfs(j)
            
        ans = 0
        seen = set()
        for i in range(n):
            if i in seen: continue
            e, v = [0], [0]
            dfs(i)
            e, v = e[0], v[0]
            ans += e==v*(v-1)
        return ans
    
    
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        G = [[] for _ in range(n)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
            
        seen = set()
        for i in range(n):
            if i in seen: continue
            Q = [i]
            seen.add(i)
            e = 0
            v = 0
            while Q:
                x = Q.pop(0)
                v += 1
                # will count edges twice
                e += len(G[x])
                for y in G[x]:
                    if y not in seen:
                        seen.add(y)
                        Q.append(y)
            if v*(v-1)==e:
                ans += 1
        return ans
                        
                