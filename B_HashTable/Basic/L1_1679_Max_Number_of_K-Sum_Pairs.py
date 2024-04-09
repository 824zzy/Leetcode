""" https://leetcode.com/problems/max-number-of-k-sum-pairs/
Two sum-ish to count k-sum
Time: O(n)
"""


class Solution:
    def maxOperations(self, A: List[int], k: int) -> int:
        seen = Counter()
        ans = 0
        for x in A:
            if seen[k - x]:
                ans += 1
                seen[k - x] -= 1
            else:
                seen[x] += 1
        return ans
