""" L0
find the node that has in-degree=n-1 and out-degree=0
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inD = [0] * (n+1)
        outD = [0] * (n+1)
        inD[0] = outD[0] = float('inf')
        for i, j in trust:
            inD[j] += 1
            outD[i] += 1

        for idx, (i, j) in enumerate(zip(inD, outD)):
            if i==n-1 and j==0: return idx
        return -1