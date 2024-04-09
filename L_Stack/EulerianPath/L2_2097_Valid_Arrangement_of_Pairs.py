""" https://leetcode.com/problems/valid-arrangement-of-pairs
Hierholzer's Algorithm
"""


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        degree = defaultdict(int)  # out-degree
        for i, j in pairs:
            G[i].append(j)
            degree[i] += 1
            degree[j] -= 1

        # find node x whose out-degree is 1
        for n in degree:
            if degree[n] == 1:
                x = n
                break

        ans = []
        stk = [x]
        while stk:
            while G[stk[-1]]:
                stk.append(G[stk[-1]].pop())
            ans.append(stk.pop())
        ans.reverse()
        return [[ans[i], ans[i + 1]] for i in range(len(ans) - 1)]
