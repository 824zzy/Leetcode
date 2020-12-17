""" Same idea of 1123 from lee213
Explanatoin
Write a sub function deep(TreeNode root).
Return a pair(int depth, TreeNode subtreeWithAllDeepest)

In sub function deep(TreeNode root):

if root == null,
return pair(0, null)

if left depth == right depth,
deepest nodes both in the left and right subtree,
return pair (left.depth + 1, root)

if left depth > right depth,
deepest nodes only in the left subtree,
return pair (left.depth + 1, left subtree)

if left depth < right depth,
deepest nodes only in the right subtree,
return pair (right.depth + 1, right subtree)

Complexity
Time O(N)
Space O(height)
"""
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return 0, None
            l, r = dfs(node.left), dfs(node.right)
            if l[0]>r[0]: return l[0]+1, l[1]
            elif l[0]<r[0]: return r[0]+1, r[1]
            else: return l[0]+1, node
        return dfs(root)[1]
    
# Find deepest pathes
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.path = collections.defaultdict(list)
        def dfs(node, d, p):
            if not node:
                if p not in self.path[d]:
                    self.path[d].append(p)
                return
            dfs(node.left, d+1, p+[node])
            dfs(node.right, d+1, p+[node])
        
        dfs(root, 0, [])        
        max_path = sorted(self.path.items(), reverse=True)[0][1]
        if len(max_path)>1:
            for i, p in enumerate(zip(*max_path)):
                if len(set(p))!=1:
                    return max_path[0][i-1]
        else:
            return max_path[0][-1]