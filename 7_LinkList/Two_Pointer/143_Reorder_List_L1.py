""" https://leetcode.com/problems/reorder-list/
1. locate the mid-point
2. reverse the 2nd half
3. merge 1st and 2nd half
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        # locate the mid-point
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # reverse the second half
        prev = None
        while slow: prev, slow.next, slow = slow, prev, slow.next
        # merge first and second half
        node = head
        while prev and prev.next:
            node.next, node = prev, node.next
            prev.next, prev = node, prev.next