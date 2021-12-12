""" https://leetcode.com/problems/rings-and-rods/
dict of Counter to record how many different rings in a rod
"""
class Solution:
    def countPoints(self, A: str) -> int:
        cnt = defaultdict(Counter)
        for i in range(0, len(A), 2):
            cnt[int(A[i+1])][A[i]] += 1
        return sum([len(v.keys())==3 for k, v in cnt.items()])