""" https://leetcode.com/problems/delayed-count-of-equal-elements/
For each index i, count indices j where i+k < j <= n-1 and nums[j] == nums[i].
Build a Counter from A[k+1:] (all elements that could match index 0).
Iterate left to right: look up cnt[A[i]] for the answer, then shrink the window
by removing A[i+k+1] from the counter (it's no longer valid for the next index).
"""


class Solution:
    def delayedCount(self, A: List[int], k: int) -> List[int]:
        cnt = Counter(A[k + 1:])
        ans = [0] * len(A)
        for i in range(len(A) - k - 1):
            if cnt[A[i]] > 0:
                ans[i] += cnt[A[i]]
            cnt[A[i + k + 1]] -= 1
        return ans
