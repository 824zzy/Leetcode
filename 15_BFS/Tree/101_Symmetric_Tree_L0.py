class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = [root]
        while queue:
            newq = []
            v = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                if n.left: v.append(n.left.val)
                else: v.append(None)
                if n.right: v.append(n.right.val)
                else: v.append(None)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            if v!=v[::-1]: return False
        return True