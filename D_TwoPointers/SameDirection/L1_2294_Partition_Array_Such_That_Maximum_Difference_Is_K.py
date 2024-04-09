""" https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
Intuition: the order doesn't matter
Sort the array and greedily find valid subsequence by two pointers.
"""


class Solution:
    def partitionArray(self, A: List[int], k: int) -> int:
        A.sort()
        mx, mn = A[0], A[0]
        ans = 1

        for x in A:
            mx = max(mx, x)
            mn = min(mn, x)
            if mx - mn > k:
                ans += 1
                mx = mn = x
        return ans
