class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            if p.next.val <= p.next.next.val:
                p = p.next
            else:
                curr = p.next.next
                temp = dummy
                p.next.next = curr.next
                while temp.next.val<=curr.val:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
        return dummy.next