""" L1: the same as 2024.
boundary equation: j-i+1>max(cnt.values())+k
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        cnt = Counter()
        for j in range(len(s)):
            cnt[s[j]] += 1
            if j-i+1>max(cnt.values())+k:
                cnt[s[i]] -= 1
                i += 1
        return len(s)-i