class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rowl = len(mat)
        coll = len(mat[0])
        ans = [[0 for i in range(coll)] for j in range(rowl)]

        for r in range(rowl):
            for c in range(coll):
                if r - 1 >= 0:
                    mat[r][c] += mat[r-1][c]
                if c - 1 >= 0:
                    mat[r][c] += mat[r][c-1]
                if c-1 >=0 and r-1 >= 0:
                    mat[r][c] -= mat[r-1][c-1]
                    
        for r in range(rowl):
            for c in range(coll):
                rl = max(0, r - K)
                rr = min(r + K, rowl-1)
                cl = max(0, c - K)
                cr = min(c + K, coll-1)

                A, B, C = 0, 0, 0
                D = mat[rr][cr]
                
                if rl - 1 >= 0:
                    B = mat[rl-1][cr]
                if cl - 1 >= 0:
                    C = mat[rr][cl - 1]
                if rl - 1 >= 0 and cl - 1 >= 0:
                    A = mat[rl - 1][cl - 1]
                    
                ans[r][c] = A + D - B - C
                
        return ans