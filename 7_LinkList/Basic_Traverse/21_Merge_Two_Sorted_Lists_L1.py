# Amazon
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = dummy = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        if l1: ans.next = l1
        if l2: ans.next = l2
        return dummy.next