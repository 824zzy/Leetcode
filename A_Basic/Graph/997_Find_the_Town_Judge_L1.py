""" https://leetcode.com/problems/find-the-town-judge/
find the node that has in-degree=n-1 and out-degree=0
"""
class Solution:
    def findJudge(self, n: int, A: List[List[int]]) -> int:
        inD = [0] * (n+1)
        outD = [0] * (n+1)
        for i, j in A: 
            inD[j] += 1
            outD[i] += 1
        
        for i, (ii, oo) in enumerate(zip(inD, outD)):
            if i and ii==n-1 and oo==0: return i
        return -1