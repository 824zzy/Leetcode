class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        curr = head
        l = 1
        while curr.next:
            curr = curr.next
            l += 1
        curr.next = head
        
        for i in range(l-k % l - 1):
            head = head.next
        ans = head.next
        head.next = None
        return ans


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
                return head
            l = 0
            t = head
            while t:
                t = t.next
                l += 1
            k = k % l
            if not k:
                return head
            curr = prev = head
            while curr.next:
                while k>0 and curr.next:
                    curr = curr.next
                    k -= 1
                if curr.next:
                    curr = curr.next
                    prev = prev.next
            ans = prev.next
            prev.next = None
            curr.next = head
            return ans