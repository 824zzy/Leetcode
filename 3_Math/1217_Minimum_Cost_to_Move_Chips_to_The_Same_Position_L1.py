class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum([1 for i in range(len(position)) if position[i]%2==0]), sum([1 for j in range(len(position)) if position[j]%2!=0]))