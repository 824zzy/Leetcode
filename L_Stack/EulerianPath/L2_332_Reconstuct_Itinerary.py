""" https://leetcode.com/problems/reconstruct-itinerary/
Hierholzer's Algorithm to find Eulerian Path
"""
from header import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = defaultdict(list)
        for i, j in tickets:
            G[i].append(j)

        for i in G:
            G[i] = sorted(G[i], reverse=True)  # make sure lexical order

        ans = []
        stk = ["JFK"]
        while stk:
            while G[stk[-1]]:
                stk.append(G[stk[-1]].pop())
            ans.append(stk.pop())
        return ans[::-1]


# It can also be solved by backtracking, but it's slower
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = defaultdict(list)
        cnt = Counter()
        for i, j in tickets:
            cnt[i + ' ' + j] += 1
            G[i].append(j)

        for k in G:
            G[k] = sorted(G[k])

        stk = ["JFK"]

        def dfs(x):
            if len(stk) == len(tickets) + 1:
                return stk
            for y in G[x]:
                if cnt[x + ' ' + y] > 0:
                    cnt[x + ' ' + y] -= 1
                    stk.append(y)
                    if dfs(y):
                        return stk
                    stk.pop()
                    cnt[x + ' ' + y] += 1
        return dfs('JFK')


"""
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
[["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
"""
