""" https://leetcode.com/problems/best-poker-hand/
match cases by counter and set
"""
class Solution:
    def bestHand(self, R: List[int], S: List[str]) -> str:
        cnt = Counter(R)
        if len(set(S))==1: return "Flush"
        elif any([v>=3 for k, v in cnt.items()]): return "Three of a Kind"
        elif any([v==2 for k, v in cnt.items()]): return "Pair"
        else: return "High Card"