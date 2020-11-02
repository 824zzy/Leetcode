class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = ''
        curr = head
        while curr:
            n += str(curr.val)
            curr = curr.next
        return int(n, 2)