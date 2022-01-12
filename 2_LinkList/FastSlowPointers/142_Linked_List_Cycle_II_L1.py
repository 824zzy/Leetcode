""" https://leetcode.com/problems/linked-list-cycle-ii/
if find cycle then detect from start
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None: return None
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                fast = head
                while slow!=fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None