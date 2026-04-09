""" https://leetcode.com/problems/h-index/
bucket sort: since h <= n, bucket each citation into [0..n] (saturating at n),
then sweep from high to low accumulating count. Return the first h where
count >= h. O(n) time, O(n) space, beats the sort-and-scan O(n log n).
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            bucket[min(c, n)] += 1
        count = 0
        for h in range(n, -1, -1):
            count += bucket[h]
            if count >= h:
                return h
