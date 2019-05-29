""" naive stack solution
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        dummy = head
        while dummy:
            stack.append(dummy.val)
            dummy = dummy.next
        for i, j in zip(stack, reversed(stack)):
            if i != j:
                return False
        return True


""" another solution
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        stack = []
        fast = slow = head
        
        while fast and fast.next:
            stack.append(slow.val)
            fast, slow = fast.next.next, slow.next
        
        if fast:
            slow = slow.next
        
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        
        return True
        