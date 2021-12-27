""" https://leetcode.com/problems/minimum-height-trees
remove leaves by iteration until there are no new leaves
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        
        G = defaultdict(list)
        inD = [0] * n
        for x, y in edges:
            G[y].append(x)
            G[x].append(y)
            inD[x] += 1
            inD[y] += 1
            
        Q = [i for i, d in enumerate(inD) if d==1]
        
        ans = []
        while Q:
            new_nodes = []
            for _ in range(len(Q)):
                i = Q.pop(0)
                ans.append(i)
                for j in G[i]:
                    inD[j] -= 1
                    if inD[j]==1: new_nodes.append(j)
            Q = new_nodes
            if new_nodes: ans = []
        return ans