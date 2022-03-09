""" https://leetcode.com/problems/next-greater-node-in-linked-list/
monotonic decreasing stack + linked list
"""
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stk = []
        ans = []
        i = 0
        while head:
            ans.append(0)
            while stk and stk[-1][1]<head.val:
                ii, _ = stk.pop()
                ans[ii] = head.val
            stk.append([i, head.val])
            head = head.next
            i += 1
        return ans