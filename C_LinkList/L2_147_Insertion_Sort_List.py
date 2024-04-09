""" https://leetcode.com/problems/insertion-sort-list
https://leetcode.com/problems/insertion-sort-list/discuss/715153/Python3-O(N2)-algo
"""


class Solution:
    def insertionSortList(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode(-inf, next=head)
        while node.next:
            if node.val <= node.next.val:
                node = node.next
            else:
                tmp = node.next
                pre = ans
                while pre.next and pre.next.val <= tmp.val:
                    pre = pre.next
                node.next = node.next.next
                tmp.next = pre.next
                pre.next = tmp

        return ans.next
