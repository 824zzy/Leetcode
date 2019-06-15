""" Basic usage of most_common()
"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s).most_common()
        
        ans = ''
        for k, v in c:
            ans += k * v
        return ans
