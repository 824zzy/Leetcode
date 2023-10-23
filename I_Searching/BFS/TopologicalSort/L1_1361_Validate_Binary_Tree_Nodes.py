""" https://leetcode.com/problems/validate-binary-tree-nodes/
valid tree check + topological sort
"""
from header import *

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        G = defaultdict(list)
        inD = [0]*n
        for i, x in enumerate(leftChild):
            if x!=-1:
                G[i].append(x)
                inD[x] += 1
        for i, x in enumerate(rightChild):
            if x!=-1:
                G[i].append(x)
                inD[x] += 1
        # in-degree cannot larger than 1
        if any(x>1 for x in inD): return False
        Q = [i for i, x in enumerate(inD) if x==0]
        # ensure only one root
        if len(Q)!=1: return False
        # topological sort
        seen = {Q[0]}
        while Q:
            i = Q.pop(0)
            for j in G[i]:
                inD[j] -= 1
                if inD[j]==0:
                    Q.append(j)
                    seen.add(j)
        return len(seen)==n
    
"""
4
[1,-1,3,-1]
[2,-1,-1,-1]
4
[1,-1,3,-1]
[2,3,-1,-1]
2
[1,0]
[-1,-1]
4
[1,0,3,-1]
[-1,-1,-1,-1]
"""