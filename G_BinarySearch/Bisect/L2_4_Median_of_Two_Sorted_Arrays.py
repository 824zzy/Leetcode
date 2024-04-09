""" https://leetcode.com/problems/median-of-two-sorted-arrays/
TODO: add log(min(m, n)) solution
"""
# binary search
import heapq


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        n = (len(A) + len(B)) // 2 + 1
        l = len(A) + len(B)
        ans = []
        while n > 0 and A and B:
            if A[0] < B[0]:
                bisect.insort(ans, A.pop(0))
            else:
                bisect.insort(ans, B.pop(0))
            n -= 1

        if n and A:
            ans.extend(A[:n])
        elif n and B:
            ans.extend(B[:n])

        if l & 1:
            return ans[-1]
        else:
            return (ans[-1] + ans[-2]) / 2


# Heap solution


class Solution:
    def findMedianSortedArrays(
            self,
            nums1: List[int],
            nums2: List[int]) -> float:
        n, heap = (len(nums1) + len(nums2)) // 2, []
        for i in nums1 + nums2:
            heapq.heappush(heap, i)

        for _ in range(n):
            t = heapq.heappop(heap)

        if n == 0:
            return heapq.heappop(heap)

        if (len(nums1) + len(nums2)) % 2 != 0:
            return heapq.heappop(heap)
        else:
            return (t + heapq.heappop(heap)) / 2
