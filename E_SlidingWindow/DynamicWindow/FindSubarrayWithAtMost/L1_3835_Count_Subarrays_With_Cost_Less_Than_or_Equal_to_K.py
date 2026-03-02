""" https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/
Sliding Window + Monotonic Queue/Heap

cost = (max - min) * length. As the window expands right, cost can only increase
(both max-min and length grow), so we can shrink from the left.
Sol1: Two heaps with lazy deletion for window max/min. O(n log n).
Sol2: Two monotonic deques for window max/min. O(n).
"""


# Sol1: Heap with lazy deletion
class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        i = 0
        mx_heap, mn_heap = [], []
        ans = 0
        for j in range(len(A)):
            heappush(mx_heap, (-A[j], j))
            heappush(mn_heap, (A[j], j))
            while (-mx_heap[0][0] - mn_heap[0][0]) * (j - i + 1) > k:
                while mx_heap[0][1] <= i:
                    heappop(mx_heap)
                while mn_heap[0][1] <= i:
                    heappop(mn_heap)
                i += 1
            ans += j - i + 1
        return ans


# Sol2: Monotonic deque
class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        i = 0
        mx_dq, mn_dq = deque(), deque()
        ans = 0
        for j in range(len(A)):
            while mx_dq and A[mx_dq[-1]] <= A[j]:
                mx_dq.pop()
            while mn_dq and A[mn_dq[-1]] >= A[j]:
                mn_dq.pop()
            mx_dq.append(j)
            mn_dq.append(j)
            while (A[mx_dq[0]] - A[mn_dq[0]]) * (j - i + 1) > k:
                i += 1
                if mx_dq[0] < i:
                    mx_dq.popleft()
                if mn_dq[0] < i:
                    mn_dq.popleft()
            ans += j - i + 1
        return ans
