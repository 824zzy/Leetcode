""" L0
Simulate the rules
"""
class Solution:
    def isValidSudoku(self, A: List[List[str]]) -> bool:
        def check_line(line):
            seen = [0] * 10
            for n in line:
                if n!='.':
                    if seen[int(n)]: return False
                    else: seen[int(n)] = 1
            return True
            
        for row in A:
            if not check_line(row): return False
                        
        for col in zip(*A):
            if not check_line(col): return False
        
        for i in range(0, len(A), 3):
            for j in range(0, len(A), 3):
                square = [A[i+k//3][j+k%3] for k in range(9)]
                if not check_line(square): return False
        
        return True