""" https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
"""

from header import *


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        ans = pre = ListNode(next=head)
        node = pre.next
        while node:
            if node.val in nums:
                node = node.next
                pre.next = node
            else:
                pre = pre.next
                node = node.next

        return ans.next
