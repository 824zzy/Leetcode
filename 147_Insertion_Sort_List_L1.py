class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            if pre.next.val < pre.next.next.val:
                pre = pre.next
            else:
                