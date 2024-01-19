""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
level order traversal with previous node
"""
from header import *
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        Q = [root]
        while Q:
            nextQ = []
            pre = None
            for node in Q:
                if not pre: pre = node
                else: 
                    pre.next = node
                    pre = node
                
                if node.left: nextQ.append(node.left)
                if node.right: nextQ.append(node.right)
            Q = nextQ     
        return root
    

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        mp = defaultdict(list)
        def dfs(node, d):
            if not node:
                return 
            mp[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        
        for _, v in mp.items():
            for i in range(1, len(v)):
                v[i-1].next = v[i]
        return root