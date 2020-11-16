# optimal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root  
    
# iterative
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = [root]
        while q:
            cur = q.pop(0)
            if cur.left and cur.right:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                q.append(cur.left)
                q.append(cur.right)
        return root
    
# extra space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level_tree = collections.defaultdict(list)
        def dfs(node, d):
            if not node:
                return 
            level_tree[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)

        for dep, lvl in level_tree.items():
            for i in range(len(lvl)-1):
                lvl[i].next = lvl[i+1]
        return root