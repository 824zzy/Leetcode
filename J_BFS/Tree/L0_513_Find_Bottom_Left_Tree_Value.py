class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        ans = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if i==0: ans = cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return ans