""" https://leetcode.com/problems/next-greater-node-in-linked-list/
monotonic decreasing stack + linked list
"""


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nextGreater = []
        stk = []
        idx = 0
        while head:
            nextGreater.append(0)
            while stk and stk[-1][1] < head.val:
                nextGreater[stk.pop()[0]] = head.val
            stk.append((idx, head.val))
            head = head.next
            idx += 1
        return nextGreater
