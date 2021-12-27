""" https://leetcode.com/problems/reverse-nodes-in-k-group/
TODO: add in-place, O(1) space complexity solution
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        stk = []
        while node:
            pre = node
            while pre and len(stk)<k:
                stk.append(pre.val)
                pre = pre.next
            if len(stk)!=k: break
            while stk:
                node.val = stk.pop()
                node = node.next
        return head