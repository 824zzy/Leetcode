class Solution:
    def countGoodRectangles(self, A: List[List[int]]) -> int:
        mins = [min(a) for a in A]
        t = max(mins)
        return mins.count(t)
