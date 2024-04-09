class Solution:
    def distributeCandies(self, A: List[int]) -> int:
        return int(min(len(A) / 2, len(Counter(A).keys())))
