# start from bottom left corner and search the target.
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        x, y = len(A)-1, 0
        while x>=0 and y<len(A[0]):
            if A[x][y]==t: return True
            elif A[x][y]>t: x -= 1
            else: y += 1
        return False
    
    
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        for r in A:
                if t>r[-1]: continue
                if t<r[0]: return False
                for n in r:
                    if n==t: return True
            return False