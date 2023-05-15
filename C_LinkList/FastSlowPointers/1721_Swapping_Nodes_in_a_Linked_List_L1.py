""" https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
fast slow pointers: 
1. fast pointer first go k step to find the left node
2. move fast and slow pointer together to find right node.
"""
from header import *

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = fast = slow = ListNode(next=head)
        for _ in range(k):
            fast = fast.next
        
        left = fast
        while fast:
            fast = fast.next
            slow = slow.next
        
        left.val, slow.val = slow.val, left.val
        return ans.next