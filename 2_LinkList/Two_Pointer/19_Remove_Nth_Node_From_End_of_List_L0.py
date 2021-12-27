class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = fast = slow = ListNode(-1)
        dummy.next = head
        
        for _ in range(n): fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next