""" http://lkw222.pythonanywhere.com/question_detail/parallel-courses/
topological sort, using in-degree to check whether all the nodes are visited
"""
from header import *


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        G = defaultdict(list)
        inD = [0] * (n + 1)
        for i, j in relations:
            G[i].append(j)
            inD[j] += 1

        Q = [i for i, x in enumerate(inD) if i and x == 0]
        if not Q:  # check cycle
            return -1
        ans = 0
        while Q:
            nxtQ = []
            for i in Q:
                for j in G[i]:
                    inD[j] -= 1
                    if inD[j] == 0:
                        nxtQ.append(j)
            Q = nxtQ
            ans += 1
        return -1 if any(inD) else ans
