""" L1
Use counter to find doubled pairs increasingly based on absolute value.
"""
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for x in sorted(cnt, key=abs):
            if cnt[x]>cnt[2*x]: return False
            cnt[2*x] -= cnt[x]
        return True
