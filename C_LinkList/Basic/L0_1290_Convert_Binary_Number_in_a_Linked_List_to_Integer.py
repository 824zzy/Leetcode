""" https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans <<= 1
            if head.val == 1:
                ans |= 1
            head = head.next
        return ans
