""" https://leetcode.com/problems/the-latest-time-to-catch-a-bus/submissions/
learn from guan: https://www.youtube.com/watch?v=dS327rmdohQ

Use two pointers to simulate the bus.
"""
class Solution:
    def latestTimeCatchTheBus(self, B: List[int], P: List[int], c: int) -> int:
        B.sort()
        P.sort()
        
        j = 0
        ans = -1
        for i in range(len(B)):
            cc = c
            while j<len(P) and P[j]<=B[i] and cc>0:
                if not j or (j and P[j-1]!=P[j]-1):
                    ans = max(ans, P[j]-1)
                cc -= 1
                j += 1
        
        if cc and (not j or (j and P[j-1]!=B[i])):
            ans = max(ans, B[i])
        return ans