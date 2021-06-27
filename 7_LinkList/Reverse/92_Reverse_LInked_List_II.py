""" L1
tmp = cur.next
cur.next = tmp.next
tmp.next = pre.next
pre.next = tmp
"""
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        for _ in range(m-1): pre = pre.next
        cur = pre.next
        for _ in range(n-m):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next