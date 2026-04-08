""" https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
prefix sum + hashmap: if two prefixes are equal, the segment between them
sums to zero. store {prefix_sum: node} and on a hit, rewire past the segment.
must also purge the removed segment's intermediate prefix sums from the map
so later hits don't point into dead nodes.
"""


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode(next=head)
        cnt = {0: dummy}
        pre = 0
        while head:
            pre += head.val
            if pre in cnt:
                # clean up prefix sums for the removed segment
                node = cnt[pre].next
                p = pre
                while node != head:
                    p += node.val
                    if p != pre:       # don't delete the one we're keeping
                        del cnt[p]
                    node = node.next
                cnt[pre].next = head.next
            else:
                cnt[pre] = head
            head = head.next
        return ans.next
