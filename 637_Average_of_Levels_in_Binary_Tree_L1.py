from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.d = defaultdict(int)
        
        def dfs(node: TreeNode, dept: int) -> None:
            if not node:
                return
            self.d[dep].append(node.val)
            
            dfs(node.left, dept+1)
            dfs(node.right, dept+1)
        
        dfs(root, 0)
        
        return [sum(l)/len(l) for l in self.d.values()]