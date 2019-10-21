""" Delete op like P203
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = pre = ListNode(float('inf'))
        pre.next = curr = head
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                pre = pre.next
        return ans.next

""" basic solution with list
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        appeared = []
        while head:
            if head.val not in appeared:
                appeared.append(head.val)
            head = head.next
        return appeared