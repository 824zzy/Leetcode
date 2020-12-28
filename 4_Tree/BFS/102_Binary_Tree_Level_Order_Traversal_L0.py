""" Iteration: use For loop to record level nodes
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                ans.append(curr)
        return ans