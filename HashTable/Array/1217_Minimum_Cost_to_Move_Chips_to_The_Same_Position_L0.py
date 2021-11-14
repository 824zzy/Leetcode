class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = Counter(position)
        o, e = 0, 0
        for k, v in cnt.items():
            if k%2==0: e += v
            else: o += v
        return min(o, e)