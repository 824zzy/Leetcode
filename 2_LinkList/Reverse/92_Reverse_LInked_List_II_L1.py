""" https://leetcode.com/problems/reverse-linked-list-ii/
1. locate the left position node
2. reverse nodes in the middle
3. reconnect the reversed nodes
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = node = ListNode(next=head)
        # locate the left position node
        prev = None
        for _ in range(left):
            prev = node
            node = node.next
        # reverse nodes in the middle
        pp, nn = prev, node
        for _ in range(left, right+1):
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        # reconnect the reversed nodes
        pp.next = prev
        nn.next = node
        return ans.next
    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = ListNode(next=head)
        prev = None
        for _ in range(left-1): head, prev = head.next, head
            
        pp, nn = prev, head
        for _ in range(left, right+1): head.next, head, prev = prev, head.next, head

        pp.next, nn.next = prev, head
        return ans.next 