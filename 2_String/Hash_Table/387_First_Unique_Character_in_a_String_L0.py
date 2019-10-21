from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

""" Old solution on 4/*/19
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_d = {}
        for c in s:
            if c in freq_d:
                freq_d[c] += 1
            else:
                freq_d[c] = 1
                
        for k, v in freq_d.items():
            if v == 1:
                return s.find(k)
        return -1