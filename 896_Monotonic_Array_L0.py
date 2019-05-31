""" Facebook naive question
"""

"""
a tons of code but efficient
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        mode = 0
        if A[-1]-A[0] > 0:
            mode = 1
        if mode == 1:
            for i in range(len(A)-1):
                if A[i] > A[i+1]:
                    return False
            return True
        else:
            for i in range(len(A)-1):
                if A[i] < A[i+1]:
                    return False
            return True


"""
more clever code but inefficient
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        dec = True
                
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                inc = False
            if A[i] < A[i+1]:
                dec = False
        return inc or dec
        
