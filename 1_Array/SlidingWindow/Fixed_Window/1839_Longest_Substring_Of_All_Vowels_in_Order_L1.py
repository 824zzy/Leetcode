"""
Usage of groupby
"""
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 0
        A = [[c, len(list(s))] for c, s in itertools.groupby(word)]
        for i in range(len(A)-4):
            if ''.join([A[j][0] for j in range(i, i+5)])=='aeiou':
                ans = max(ans, sum([A[j][1] for j in range(i, i+5)]))
        return ans