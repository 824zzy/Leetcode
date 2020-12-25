# recursive
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        new = head.next
        head.next = self.swapPairs(new.next)
        new.next = head
        return new

# iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head2 = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
            
        return head2