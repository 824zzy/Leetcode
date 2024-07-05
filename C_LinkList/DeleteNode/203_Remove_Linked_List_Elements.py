""" L1: https://leetcode.com/problems/remove-linked-list-elements/
If node.next.val == val, remove node.next; otherwise, move node to the next node.
"""


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = node = ListNode(next=head)
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return ans.next
