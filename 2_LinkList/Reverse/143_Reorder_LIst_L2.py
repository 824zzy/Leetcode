""" https://leetcode.com/problems/reorder-list/
It takes 3 steps to achive O(N) time and O(1) space for this problem.

locate the mid-point;
reverse the 2nd half;
merge 1st and 2nd half.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next
        
        node = head
        while prev and prev.next:
            node.next, node = prev, node.next
            prev.next, prev = node, prev.next
            