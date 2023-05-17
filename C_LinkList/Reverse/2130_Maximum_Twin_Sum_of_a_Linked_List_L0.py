""" https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
fast-slow pointers to find middle point and reverse the first half 
"""
from header import *

# O(1) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle point
        fast = slow = head
        cnt = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            cnt += 1
        # reverse first half
        pre, node = None, head
        for _ in range(cnt): pre, node.next, node = node, pre, node.next
        # find maximum twin sum        
        ans = 0
        while pre:
            ans = max(ans, pre.val+slow.val)
            pre = pre.next
            slow = slow.next
        return ans

# O(n) space    
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        return max([A[i]+A[~i] for i in range(len(A)//2)])