class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        deque = [root]
        miss = False
        while deque:
            curr = deque.pop(0)
            if not curr:
                miss = True
            else:
                if miss==True:
                    return False
                deque.append(curr.left)
                deque.append(curr.right)
        return True