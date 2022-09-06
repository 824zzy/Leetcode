""" https://leetcode.com/problems/jump-game-vi/
The maximum score we can get when we reached index i is equal to nums[i] + maximum among previous k (or less if we reached boundary) numbers.
So maintain a monotonic max heap to always keep valid optimal element in heap top
"""
class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        ans = [0] * len(A)
        ans[0] = A[0]
        pq = [[-A[0], 0]]
        for i in range(1, len(A)):
            while i-pq[0][1]>k: heappop(pq)
            ans[i] = A[i] + ans[pq[0][1]]
            heappush(pq, [-ans[i], i])
        return ans[-1]