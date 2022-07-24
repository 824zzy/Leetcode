""" https://leetcode.com/problems/equal-row-and-column-pairs/
1. Consider rows and columns as strings, and count their frequencies.
2. Count the equal row and column pairsb based on the frequencies.
"""
class Solution:
    def equalPairs(self, A: List[List[int]]) -> int:
        rows = Counter()
        cols = Counter()
        for r in A:
            rows[' '.join(str(x) for x in r)] += 1
        for c in zip(*A):
            cols[' '.join(str(x) for x in c)] += 1
        ans = 0
        for r in rows:
            if r in cols: ans += rows[r]*cols[r]
        return ans