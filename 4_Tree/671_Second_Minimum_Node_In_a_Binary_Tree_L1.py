class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        q, minDiff = [root], float('inf')
        for node in q:
            if node.left:
                if node.left.val==node.val:
                    q.append(node.left)
                else:
                    minDiff = min(node.left.val, minDiff)
                if node.right.val == node.val:
                    q.append(node.right)
                else:
                    minDiff = min(node.right.val, minDiff)
        return -1 if minDiff==float('inf') else minDiff