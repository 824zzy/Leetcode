from collections import Counter


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.sm = []

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                self.sm.append(node.val)
                return node.val
            l = dfs(node.left)
            r = dfs(node.right)
            self.sm.append(l + r + node.val)
            return l + r + node.val

        dfs(root)
        cnt = Counter(self.sm)
        max_freq = max(cnt.values())
        return [k for k, v in cnt.items() if v == max_freq]


# After cleaning


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            s = l + r + node.val
            self.cnt[s] += 1
            return s

        self.cnt = Counter()
        dfs(root)
        max_freq = max(self.cnt.values())
        return [k for k, v in self.cnt.items() if v == max_freq]
