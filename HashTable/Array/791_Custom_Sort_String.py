""" L1
Simply use counter to simulate string formation
"""
class Solution:
    def customSortString(self, order: str, S: str) -> str:
        cnt, s = Counter(S), set(order)
        return ''.join([o*cnt[o] for o in order])+''.join([c*cnt[c]for c in cnt if c not in s])