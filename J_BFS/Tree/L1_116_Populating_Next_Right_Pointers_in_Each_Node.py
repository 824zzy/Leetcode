""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
find right node by next: `if node.next: node.right.next = node.next.left`
""" 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node or not node.left: return node
            node.left.next = node.right
            if node.next: node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
            return node
        
        return dfs(root)
    
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