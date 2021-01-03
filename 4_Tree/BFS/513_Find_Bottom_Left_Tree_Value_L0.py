class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        ans = 0
        while queue:
            `possible logic`
            for i in range(len(queue)):
                cur = queue.pop(0)
                `possible logic`
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                `possible logic`
        return ans