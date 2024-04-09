""" https://leetcode.com/problems/sort-list/
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        A = []
        while head:
            A.append(head.val)
            head = head.next

        A = sorted(A)
        node = ans = ListNode()
        for x in A:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        return ans.next
