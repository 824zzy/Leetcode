""" L1: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
fast slow pointers: fast pointer first go k step to find the left node, 
then move fast and slow pointer together to find right node.
"""
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(next=head)
        fast = slow = ans
        for _ in range(k): fast = fast.next
        left = fast
        
        while fast: fast, slow = fast.next, slow.next
        slow.val, left.val = left.val, slow.val
        return ans.next