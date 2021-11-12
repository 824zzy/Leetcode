class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans, s, pos = [], [], -1
        while head:
            pos += 1
            ans.append(0)
            while s and s[-1][-1]<head.val:
                idx, _ = s.pop()
                ans[idx] = head.val
            s.append([pos, head.val])
            head = head.next
        return ans