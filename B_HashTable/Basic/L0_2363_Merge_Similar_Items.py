""" https://leetcode.com/problems/merge-similar-items/
merge similar items by hash table
"""
class Solution:
    def mergeSimilarItems(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for k, v in A+B:
            cnt[k] += v
        return [[k, v] for k, v in sorted(cnt.items())]