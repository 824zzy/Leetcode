""" https://leetcode.com/problems/find-all-people-with-secret/
"""
from header import *


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            Q = set()
            G = defaultdict(list)
            for x, y, _ in grp:
                G[x].append(y)
                G[y].append(x)
                if x in can:
                    Q.add(x)
                if y in can:
                    Q.add(y)
            Q = deque(Q)
            while Q:
                x = Q.popleft()
                for y in G[x]:
                    if y not in can:
                        can.add(y)
                        Q.append(y)
        return can
