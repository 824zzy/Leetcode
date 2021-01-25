# Facebook: use heap to maintain a total order of each linklist.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp = []
        for l in lists:
            while l:
                heapq.heappush(hp, l.val)
                l = l.next
        ans = curr = ListNode(-1)
        while hp:
            curr.next = ListNode(heapq.heappop(hp))
            curr = curr.next
        return ans.next

# sort all values in a list
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        nums = sorted(nums)
        ans = curr = ListNode(-1)
        for n in nums:
            curr.next = ListNode(n)
            curr = curr.next
        return ans.next