""" https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
fast slow pointers, use pre to save previous node before slow pointer
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        fast, slow = head, head
        pre = ListNode(next=slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            pre = pre.next
        pre.next = pre.next.next
        return head