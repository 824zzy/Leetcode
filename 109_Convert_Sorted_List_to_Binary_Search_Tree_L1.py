"""
1. fast slow pointer with previous tracker
2. variant recursion compared to 108
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid = self.findMid(head)
        root = TreeNode(mid.val)
        
        root.left = sortedListToBST(head)
        root.right = sortedListToBST(mid.next)
        
        return root

    def findMid(self, head: ListNode) -> TreeNode:
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = None
        return slow