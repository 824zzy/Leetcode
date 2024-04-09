""" https://leetcode.com/problems/max-number-of-k-sum-pairs/
Different direction two pointer to count k-sum
Time: O(nlogn)
"""


class Solution:
    def maxOperations(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 0
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] + A[r] == k:
                ans += 1
                l, r = l + 1, r - 1
            elif A[l] + A[r] < k:
                l += 1
            else:
                r -= 1
        return ans
