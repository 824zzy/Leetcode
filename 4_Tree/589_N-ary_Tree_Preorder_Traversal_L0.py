# Trivial recursive solution
class Solution:
    def __init__(self):
        self.ans = []
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        self.ans.append(root.val)
        for c in root.children:
            self.preorder(c)
        return self.ans