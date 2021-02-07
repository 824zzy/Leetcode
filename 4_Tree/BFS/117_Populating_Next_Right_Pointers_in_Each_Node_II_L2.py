class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ans = []
        if root is None:
            return 
    
        q = [[root]]    
        while q:
            nodes = q.pop(0)
            level_nodes = []
            for node in nodes:
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            size = len(level_nodes)
            if size > 0:
                for i in range(size-1):
                    level_nodes[i].next = level_nodes[i+1]
                q.append(level_nodes)
        return root
