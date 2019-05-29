""" implement with stack
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        if len(stack) == 0:
            return []
        t = rl = ListNode(stack[-1])
        stack.pop()
        for i in range(len(stack)):
            new_node = ListNode(stack[-1])
            t.next = new_node
            t = t.next
            stack.pop()
        return rl


""" while loop(28ms) is better than for loop(48ms)
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
        dummy = res = ListNode(-1)
        
        while stack:
            dummy.next = ListNode(stack.pop())
            dummy = dummy.next
        return res.next
        
        