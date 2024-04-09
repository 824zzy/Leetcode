""" https://leetcode.com/problems/merge-nodes-in-between-zeros/
simulate the process of merging nodes between zeros
"""


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = pre = ListNode()
        node = head
        while node:
            node = node.next
            sm = 0
            while node and node.val != 0:
                sm += node.val
                node = node.next
            if sm:
                pre.next = ListNode(sm)
                pre = pre.next
        return ans.next
