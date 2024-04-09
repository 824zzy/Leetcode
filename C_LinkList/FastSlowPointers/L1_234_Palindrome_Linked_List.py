""" https://leetcode.com/problems/palindrome-linked-list/
1. use fast slow pointer to split linked list
2. reverse the second half and compare.
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # locate middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse: r, m, l = l, r, m
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        # check palindrome
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
