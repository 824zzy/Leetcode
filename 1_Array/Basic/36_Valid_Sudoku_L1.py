class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        if not self.checkRows(board):
            return False
        if not self.checkCols(board):
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkRegion(board, i, j):
                    return False
        return True
        
    def checkRegion(self, board, x, y):
        seen = set()
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        return True
            
    def checkCols(self, grid):
        for j in range(9):
            seen = set()
            for i in range(9):
                if grid[i][j]!='.':
                    if grid[i][j] in seen:
                        return False
                    else:
                        seen.add(grid[i][j])
        return True
        
    def checkRows(self, grid):
        for i in range(9):
            seen = set()
            for v in grid[i]:
                if v!='.':
                    if v in seen:
                        return False
                    else:
                        seen.add(v)
        return True
