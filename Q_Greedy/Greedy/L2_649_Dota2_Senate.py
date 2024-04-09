""" https://leetcode.com/problems/dota2-senate/
greedily simulate by two queues
"""


class Solution:
    def predictPartyVictory(self, A: str) -> str:
        R, D = [], []
        for i, x in enumerate(A):
            if x == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            if R[0] < D[0]:
                R.append(R.pop(0) + len(A))
                D.pop(0)
            else:
                R.pop(0)
                D.append(D.pop(0) + len(A))
        return "Radiant" if R else "Dire"


"""
"RD"
"RDD"
"DDRRRR"
"RRDDD"
"DRRDRDRDRDDRDRDR"
"""
