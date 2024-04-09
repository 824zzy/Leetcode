class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 for i in zip(heights, sorted(heights)) if i[0] != i[1]])
