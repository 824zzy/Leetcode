""" L1
Every part should have N/k elements, except the fist N%k parts have an extra one.
"""
# optimal solution
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        while head:
            N += 1
            head = head.next
            
        l, ext = N//k, N%k
        ans = []
        cur = head
        for i in range(k):
            tmp = cur
            for _ in range(d+(i<r)-1):
                if cur: cur = cur.next
            if cur: cur.next, cur = None, cur.next
            ans.append(tmp)
        return ans
    
# solution using extra space
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def create_list(arr):
            dummy = l = ListNode(0)
            while arr:
                l.next = ListNode(arr.pop(0))
                l = l.next
            return dummy.next
        
        A = []
        while head:
            A.append(head.val)
            head = head.next
            
        L, ext = len(A)//k, len(A)%k
        ans = []
        idx = 0
        while idx<len(A):
            if ext:
                tmp = create_list(A[idx:idx+L+1])
                idx += L+1
                ext -= 1
            else: 
                tmp = create_list(A[idx:idx+L])
                idx += L
            ans.append(tmp)
        if len(ans)<k: ans.extend([create_list([])]*(k-len(ans)))
        return ans