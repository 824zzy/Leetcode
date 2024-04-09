""" L1: https://leetcode.com/problems/linked-list-components/
only consider to count the end of component and deal with begin and end node.
"""


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while head:
            if head.val in nums and (
                    head.next is None or head.next.val not in nums):
                ans += 1
            head = head.next
        return ans
