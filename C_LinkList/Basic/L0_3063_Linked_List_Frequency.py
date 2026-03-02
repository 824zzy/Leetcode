""" https://leetcode.com/problems/linked-list-frequency/
linked list simulation
"""


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        while head:
            cnt[head.val] += 1
            head = head.next

        res = node = ListNode()
        for _, v in cnt.items():
            node.next = ListNode(v)
            node = node.next
        return res.next
