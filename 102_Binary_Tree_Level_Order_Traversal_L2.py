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

""" Recursion: use defaultdict to record level nodes
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.level_dic = defaultdict(list)
        
        def getLevel(node: TreeNode, level: int) -> None:
            if not node:
                return
            self.level_dic[level].append(node.val)
            getLevel(node.left, level+1)
            getLevel(node.right, level+1)

        getLevel(root, 1)
        return list(self.level_dic.values())