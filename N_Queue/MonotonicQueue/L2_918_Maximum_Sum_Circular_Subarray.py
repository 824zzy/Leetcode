""" https://leetcode.com/problems/maximum-sum-circular-subarray/
"""


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        prefix = list(accumulate(A * 2, initial=0))

        dq = deque([(0, prefix[0])])
        ans = A[0]
        for i in range(1, len(prefix)):
            while dq and i - dq[0][0] > len(A):
                dq.popleft()
            ans = max(ans, prefix[i] - dq[0][1])
            while dq and dq[-1][1] >= prefix[i]:
                dq.pop()
            dq.append((i, prefix[i]))
        return ans
