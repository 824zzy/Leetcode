""" https://leetcode.com/problems/clone-graph/submissions/
"""
from header import *

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        Q = [node]
        seen = {node: Node(node.val)}
        while Q:
            i = Q.pop(0)
            for j in i.neighbors:
                if j not in seen:
                    seen[j] = Node(j.val)
                    Q.append(j)
                seen[i].neighbors.append(seen[j])
        return seen[node]