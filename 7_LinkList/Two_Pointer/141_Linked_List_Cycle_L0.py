class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False