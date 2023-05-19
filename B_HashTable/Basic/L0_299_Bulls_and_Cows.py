""" https://leetcode.com/problems/bulls-and-cows/
"""
class Solution:
    def getHint(self, S: str, G: str) -> str:
        A, B = 0, 0
        seenS, seenG = Counter(), Counter()
        for s, g in zip(S, G):
            if s==g: A += 1
            else:
                seenS[s] += 1
                seenG[g] += 1
        return str(A)+'A'+str(sum((seenS&seenG).values()))+'B'