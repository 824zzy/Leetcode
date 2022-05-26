""" https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
class Codec:
    def serialize(self, root):
        if not root: return ''
        nodes = []
        Q = [root]
        while Q:
            for _ in range(len(Q)):
                cur_n = Q.pop(0)
                if type(cur_n)==str: nodes.append(cur_n)
                else: 
                    nodes.append(cur_n.val)
                    if cur_n.left: Q.append(cur_n.left)
                    else: Q.append('null')
                    if cur_n.right: Q.append(cur_n.right)
                    else: Q.append('null')
    
        return str(nodes)

    def deserialize(self, data):
        if not data: return None
        nodes = data[1:-1].split(', ')
        dummy = TreeNode(nodes.pop(0))
        Q = [dummy]
        while nodes:
            cur = Q.pop(0)
            if nodes: l = nodes.pop(0)
            if nodes: r = nodes.pop(0)
            if l!="'null'": cur.left = TreeNode(l)
            if r!="'null'": cur.right = TreeNode(r)

            if cur.left: Q.append(cur.left)
            if cur.right: Q.append(cur.right)
        
        return dummy