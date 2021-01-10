# fast slow pointers
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(k):
            fast = fast.next
        left_node = fast
        while fast:
            fast = fast.next
            slow = slow.next
        slow.val, left_node.val = left_node.val, slow.val
        
        return dummy.next
    
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l[k-1], l[-k] = l[-k], l[k-1]
        ans = ListNode(-1)
        t = ListNode(l.pop(0))
        ans.next = t
        while l:
            tmp = ListNode(l.pop(0))
            t.next = tmp
            t = t.next
        return ans.next
