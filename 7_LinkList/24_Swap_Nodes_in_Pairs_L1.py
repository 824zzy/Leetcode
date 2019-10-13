class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(head.next.next)
        second.next = head
        return second