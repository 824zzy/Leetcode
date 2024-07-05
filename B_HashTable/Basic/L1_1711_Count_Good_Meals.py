""" https://leetcode.com/problems/count-good-meals/
since meal size < 2*20, so the two meals sum won't larger than 2*21,
then use two sum-ish hash table to count good meals
Time: O(22n)
"""


class Solution:
    def countPairs(self, A: List[int]) -> int:
        seen = Counter()
        ans = 0
        for x in A:
            for i in range(22):
                ans += seen[2 ** i - x]
            seen[x] += 1
        return ans % (10 ** 9 + 7)
