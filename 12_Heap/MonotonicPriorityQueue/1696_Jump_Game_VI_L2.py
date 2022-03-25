""" https://leetcode.com/problems/jump-game-vi/
TODO: https://leetcode.com/problems/jump-game-vi/discuss/1260696/Python-Monotonic-deque-explained
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