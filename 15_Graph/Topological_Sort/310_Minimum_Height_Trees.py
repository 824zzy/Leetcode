""" L2
remove leaves by iteration until there are no new leaves
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        e = defaultdict(list)
        D = [0] * n
        for i, j in edges:
            e[j].append(i)
            e[i].append(j)
            D[i] += 1
            D[j] += 1
        
        Q = []
        for i, d in enumerate(D):
            if d==1: Q.append(i)
    
        ans = []
        while Q:
            new_leaves = []
            for i in Q:
                ans.append(i)
                for j in e[i]:
                    D[j] -= 1
                    if D[j]==1: new_leaves.append(j)
            Q = new_leaves
            if new_leaves: ans = []
        return ans