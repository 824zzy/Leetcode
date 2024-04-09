""" https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
prefix sum + binary search

Since prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j],
lower bound of j is: prefix[j] >= 2 * prefix[i]
upper bound of j is: prefix[j] <= 0.5 * (prefix[-1] + prefix[i])
"""


class Solution:
    def waysToSplit(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        prefix = list(accumulate(A))
        for i in range(len(prefix)):
            lower_j = max(bisect_left(prefix, 2 * prefix[i]), i + 1)
            upper_j = min(bisect_right(
                prefix, 0.5 * (prefix[-1] + prefix[i])), len(prefix) - 1)
            ans += max(upper_j - lower_j, 0)
        return ans % MOD


""" 1 1 3 0
[0,3,3]
[1,1,1]
[1,2,2,2,5,0]
[3,2,1]
"""
