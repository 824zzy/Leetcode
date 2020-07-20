class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sumMat = {i: sum(r) for i, r in enumerate(mat)}
        sortK = sorted(sumMat.items(), key=lambda item:item[1])
        return [sortK[i][0] for i in range(k)]