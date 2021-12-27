# Iterative solution
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        t = defaultdict(list)
        t[0] = [root.val]
        q = [root]
        d = 1
        while q:
            tmp = []
            while q:
                cur = q.pop(0)
                for c in cur.children:
                    t[d].append(c.val)
                    tmp.append(c)
            q.extend(tmp)
            d += 1
        return [v for k, v in t.items()]
                
# Recursive solution
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.t = defaultdict(list)
        def dfs(node, d):
            if not node:
                return
            self.t[d].append(node.val)
            for c in node.children:
                dfs(c, d+1)
        
        dfs(root, 0)
        return [v for k, v in self.t.items()]
