from collections import OrderedDict
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = OrderedDict()
        def dfs(node, d):
            if not node:
                return
            if d not in ans:
                ans[d] = [node.val]
            else:
                ans[d].append(node.val)
            left = dfs(node.left, d+1)
            right = dfs(node.right, d+1)
        dfs(root, 0)
        ans = [v for _, v in ans.items()]
        return ans[::-1]