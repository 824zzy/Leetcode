""" https://leetcode.com/problems/node-with-highest-edge-score/
count in-coming scores by hash table and return the highest score node with smallest index
"""
class Solution:
    def edgeScore(self, E: List[int]) -> int:
        cnt = Counter()
        for i, j in enumerate(E):
            cnt[j] += i
        return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]