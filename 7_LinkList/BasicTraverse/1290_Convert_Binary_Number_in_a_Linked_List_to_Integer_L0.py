""" https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = 2*ans + head.val
            head = head.next
        return ans
    
    
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)
