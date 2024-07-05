""" https://leetcode.com/problems/process-restricted-friend-requests/
for each request, check if they break any restrictions.
"""


class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def friendRequests(
        self, n: int, restrictions: List[List[int]], requests: List[List[int]]
    ) -> List[bool]:
        def canbefriends(ii, jj):
            for x, y in restrictions:
                xx, yy = dsu.find(x), dsu.find(y)
                if (ii == xx and jj == yy) or (ii == yy and jj == xx):
                    return False
            return True

        ans = []
        dsu = DSU(n)
        for i, j in requests:
            ii, jj = dsu.find(i), dsu.find(j)
            if not canbefriends(ii, jj):
                ans.append(False)
            else:
                ans.append(True)
                dsu.union(i, j)
        return ans
