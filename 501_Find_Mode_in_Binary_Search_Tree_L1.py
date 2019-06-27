from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.val = []
        def dfs(root: TreeNode) -> None:
            if not root:
                return
            self.val.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        counter = Counter(self.val)
        max_val = max(counter.values())
        ans = 0
        for k, v in counter.items():
            if v == max_val:
                ans += 1
        
        return ans