""" https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
while loop can be written as below:

"""
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1, t2 = [], []
        def dfs(node, l):
            if not node:
                return
            dfs(node.left, l)
            l.append(node.val)
            dfs(node.right, l)
            
        dfs(root1, t1)
        dfs(root2, t2)
        ans = []
        while t1 and t2:
            if t1[0]<t2[0]: ans.append(t1.pop(0))
            else: ans.append(t2.pop(0))
        return ans + t1 + t2