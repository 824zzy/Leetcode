""" L2
Divide and conquer along with dfs
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end):
            if start > end: return [None]
            if start == end: return [TreeNode(start)]
            result = []
            for i in range(start, end+1):
                left = dfs(start, i-1)
                right = dfs(i+1, end)
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        result.append(curr)
            return result

        return dfs(1, n)