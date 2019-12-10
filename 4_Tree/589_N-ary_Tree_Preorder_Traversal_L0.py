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

# Smarter iterative solution
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stk = [root]
        while stk:
            curr = stk.pop(0)
            if curr!=None:
                ans.append(curr.val)
                for n in reversed(curr.children):
                    stk.insert(0, n)
        return ans