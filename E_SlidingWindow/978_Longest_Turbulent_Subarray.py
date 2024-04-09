""" L1: special sliding window case
Lots of corner cases.
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        D = []
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                D.append(1)
            elif A[i] < A[i + 1]:
                D.append(-1)
            else:
                D.append(0)
        # corner cases
        if len(D) == 1:
            return 2
        elif len(set(A)) == 1:
            return 1

        i = 0
        for j in range(1, len(A) - 1):
            if D[j] == 0:
                i = j + 1
            elif D[j] == D[j - 1]:
                i = j
            ans = max(ans, j - i + 2)
        return ans


"""
[37,199,60,296,257,248,115,31,273,176]
[9,4,2,10,7,8,8,1,9]
[100]
[4,8,12,16]
[100, 100, 100]
[0,1,1,0,1,0,1,1,0,0]
[9,9]
"""
