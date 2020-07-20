""" If cycle then detect from start
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        if slow==fast:
            fast = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None

# Use seen hash map    
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = {}
        while head:
            seen[head] = head
            if seen.get(head.next, 0):
                return head.next
            head = head.next