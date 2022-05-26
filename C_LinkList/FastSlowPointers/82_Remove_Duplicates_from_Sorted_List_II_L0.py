""" https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = slow = ListNode(val=-1, next=head)
        fast = head
        while fast:
            while fast.next and fast.val==fast.next.val:
                fast = fast.next
            if slow.next==fast:
                slow = slow.next
                fast = fast.next
            else:
                slow.next = fast.next
                fast = slow.next
        return ans.next