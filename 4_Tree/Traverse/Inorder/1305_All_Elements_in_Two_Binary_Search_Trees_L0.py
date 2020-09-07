# O(N)
""" while loop can be written as below:
while t1 and t2:
    if t1[0]<t2[0]:
        ans.append(t1.pop(0))
    else:
        ans.append(t2.pop(0))
return ans + t1 + t2
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
        while t1 or t2:
            cur1 = t1[0] if t1 else float('inf')
            cur2 = t2[0] if t2 else float('inf')
            if cur1<=cur2:
                ans.append(cur1)
                if t1:
                    t1.pop(0)
            else:
                ans.append(cur2)
                if t2:
                    t2.pop(0)
        return ans
        

# O(Nlog(N))
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            self.ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root1)
        dfs(root2)
        return sorted(self.ans)
