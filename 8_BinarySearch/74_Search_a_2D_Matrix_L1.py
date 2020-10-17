class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return 0
        
        def search(l, i, j):
            while i<j:
                m = (i+j)//2
                if l[m]<target<l[m+1]:
                    return m
                if l[m]<target:
                    i = m+1
                elif l[m]>target:
                    j = m-1
                else:
                    return "find"
            return i
        
        lr = [x[0] for x in matrix]
        r = search(lr, 0, len(lr)-1)
        if r=='find': return True
        lc = matrix[r]
        c = search(lc, 0, len(lc)-1)
        return c=="find" or matrix[r][c]==target
