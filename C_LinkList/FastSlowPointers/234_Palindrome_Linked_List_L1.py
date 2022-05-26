""" https://leetcode.com/problems/palindrome-linked-list/
1. use fast slow pointer to split linked list
2. reverse the second half and compare.
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        last = slow.next
        pre = head
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp
        while slow.next:
            slow = slow.next
            if pre.val!=slow.val: return False
            pre = pre.next
        return True