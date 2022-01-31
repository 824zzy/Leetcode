""" https://leetcode.com/problems/rotate-list/
fast slow pointers.
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        l, node = 0, head
        while node: l, node = l+1, node.next
        if k:= k%l:
            slow = fast = head
            while k: fast, k = fast.next, k-1
            while fast.next: fast, slow = fast.next, slow.next
                
            fast.next, head, slow.next = head, slow.next, None
        return head