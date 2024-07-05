""" Delete op like P203
"""


class Solution(object):
    def deleteDuplicates(self, head):
        ans = pre = ListNode(float("inf"))
        pre.next = curr = head
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                pre = pre.next
        return ans.next
