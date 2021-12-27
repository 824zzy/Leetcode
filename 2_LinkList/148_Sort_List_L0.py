class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = sorted(l)
        dummy = ans = ListNode(l[0])
        for i in range(1, len(l)):
            t = ListNode(l[i])
            dummy.next = t
            dummy = t
        return ans