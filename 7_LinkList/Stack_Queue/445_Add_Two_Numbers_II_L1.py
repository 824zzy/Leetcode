class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = []
        carry = 0
        while s1 or s2 or carry:
            v1, v2 = 0, 0
            if s1:
                v1 = s1.pop()
            if s2:
                v2 = s2.pop()
            s = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            ans.append(s)
        res = dummy = ListNode(0)
        while ans:
            n = ListNode(ans.pop())
            dummy.next = n
            dummy = dummy.next
        return res.next