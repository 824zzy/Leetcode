""" easy set solution
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        ele = []
        while curr:
            ele.append(curr.val)
            curr = curr.next
            
        ele = sorted(list(set(ele)))
        res = curr = ListNode(0)
        while ele:
            node = ListNode(ele.pop(0))
            curr.next = node
            curr = node
        
        return res.next

""" basic solution with list
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        appeared = []
        while head:
            if head.val not in appeared:
                appeared.append(head.val)
            head = head.next
        return appeared