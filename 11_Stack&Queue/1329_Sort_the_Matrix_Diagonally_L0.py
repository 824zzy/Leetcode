from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diag = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diag[i-j].append(mat[i][j])
                
        for k, v in diag.items():
            diag[k] = sorted(diag[k])
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diag[i-j].pop(0)
        return mat