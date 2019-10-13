""" Stack & Iterative
1. curr pointer to store temporary variable.
2. dummy to build fake node: ListNode(-1)
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        dummy = ans = ListNode(-1)
        while stack:
            dummy.next = ListNode(stack.pop())
            dummy = dummy.next
        return ans.next

""" Pointer & Iterative
1. Reverse Routine:
    while curr:
        prev, prev.next, curr = curr, prev, curr.next
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            prev, prev.next, curr = curr, prev, curr.next
        return prev

""" Recursive solution
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        N = self.reverseList(head.next)
        head.next.next = head.next
        head.next = None
        return N