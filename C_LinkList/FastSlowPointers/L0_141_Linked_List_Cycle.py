""" https://leetcode.com/problems/linked-list-cycle/
check if fast and slow pointers can meet
"""


class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
