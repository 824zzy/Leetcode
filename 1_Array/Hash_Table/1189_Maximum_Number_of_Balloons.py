""" L1
From counter, fin the minimum letter appears the least in "balon".
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        T = Counter(text)
        target = "balon"
        ans = float('inf')
        for t in target:
            if t=='l' or t=='o': ans = min(T[t]//2, ans)
            else: ans = min(T[t], ans)
        return ans