""" https://leetcode.com/problems/merge-two-sorted-lists/
append larger l1 or l1 to ans until one of l1 and l2 becomes empty
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = dummy = ListNode(0)
        # append larger l1 or l1 to ans until one of l1 and l2 becomes empty
        while l1 and l2:
            if l1.val<l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        # append remained elements
        if l1: ans.next = l1
        if l2: ans.next = l2
        return dummy.next