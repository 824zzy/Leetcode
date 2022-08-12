""" https://leetcode.com/problems/reachable-nodes-with-restrictions/
"""
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
            
        seen = set()
        def dfs(node):
            if node in restricted: 
                return 0
            cnt = 1
            seen.add(node)
            for j in G[node]:
                if j not in seen:
                    cnt += dfs(j)
            return cnt
        
        return dfs(0)