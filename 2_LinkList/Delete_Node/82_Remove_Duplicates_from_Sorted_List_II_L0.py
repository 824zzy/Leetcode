class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode('inf')
        dummy.next = head
        curr = head
        while curr and curr.next:
            if curr.val==curr.next.val:
                toDel = curr.val
                while curr and curr.val==toDel:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next