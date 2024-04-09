""" https://leetcode.com/problems/add-two-numbers/
traverse l1 and l2 while using carry
"""


class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            carry, s = divmod(a + b + carry, 10)
            node.next = ListNode(s)
            node = node.next
        return ans.next
