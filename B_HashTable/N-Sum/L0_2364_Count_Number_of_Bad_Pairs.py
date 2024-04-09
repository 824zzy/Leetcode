""" https://leetcode.com/problems/count-number-of-bad-pairs/
Because j - i != nums[j] - nums[i] ==> nums[i] - i != nums[j] - j,
we can count "Good" pairs using hash table in N-Sum way.
"""


class Solution:
    def countBadPairs(self, A: List[int]) -> int:
        n = len(A)
        seen = Counter()
        ans = 0
        for i in range(len(A)):
            ans += seen[A[i] - i]
            seen[A[i] - i] += 1
        return n * (n - 1) // 2 - ans
