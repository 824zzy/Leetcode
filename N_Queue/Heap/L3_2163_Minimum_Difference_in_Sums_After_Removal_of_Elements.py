""" https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
from: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/discuss/1747029/Python-Explanation-with-pictures-Priority-Queue.
1. Choose the n smallest element from the nums[:k].
2. Choose the n biggest elements from the nums[k:].
3. Evaluate the difference and update ans.
"""


class Solution:
    def minimumDifference(self, A: List[int]) -> int:
        n = len(A) // 3

        # Build pre_min using min-heap.
        pre_min, cur_min = [sum(A[:n])], sum(A[:n])
        pre_hp = [-x for x in A[:n]]
        heapq.heapify(pre_hp)
        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(pre_hp)
            cur_min -= cur_pop
            cur_min += min(cur_pop, A[i])
            pre_min.append(cur_min)
            heapq.heappush(pre_hp, -min(cur_pop, A[i]))

        # Build suf_max.
        suf_max, cur_max = [sum(A[2 * n :])], sum(A[2 * n :])
        suf_hp = [x for x in A[2 * n :]]
        heapq.heapify(suf_hp)
        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(suf_hp)
            cur_max -= cur_pop
            cur_max += max(cur_pop, A[i])
            suf_max.append(cur_max)
            heapq.heappush(suf_hp, max(cur_pop, A[i]))
        suf_max = suf_max[::-1]

        # Iterate over pre_min and suf_max and get the minimum difference.
        ans = math.inf
        for a, b in zip(pre_min, suf_max):
            ans = min(ans, a - b)
        return ans
