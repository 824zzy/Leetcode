""" https://leetcode.com/problems/binary-tree-level-order-traversal/
iteration solution : use For loop to record level nodes
"""


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        Q = [root]
        ans = []
        while Q:
            tmp = []
            for _ in range(len(Q)):
                node = Q.pop(0)
                tmp.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            ans.append(tmp)
        return ans[::-1]
