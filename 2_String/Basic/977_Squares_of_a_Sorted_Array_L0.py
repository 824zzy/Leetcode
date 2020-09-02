class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = list(map(lambda a: abs(a)**2, A))
        return sorted(A)