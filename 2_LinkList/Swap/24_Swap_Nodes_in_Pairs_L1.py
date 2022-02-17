""" https://leetcode.com/problems/swap-nodes-in-pairs/
from dba: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/984392/Python-O(n)-solution-explained
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = pre = ListNode(next=head)
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            
            pre.next, b.next, a.next = b, a, b.next
            
            pre = a
        return ans.next