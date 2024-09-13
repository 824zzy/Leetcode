""" https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Delete op like P203
"""

from header import *


class Solution(object):
    def deleteDuplicates(self, head):
        ans = pre = ListNode(inf)
        pre.next = curr = head
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                pre = pre.next
        return ans.next
