""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
level order traversal with previous node
"""
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