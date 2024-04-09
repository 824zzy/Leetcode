""" https://leetcode.com/problems/kill-process/
build a graph-like tree, then start from kill node to find all the children
"""
from header import *


class Solution:
    def killProcess(
            self,
            pid: List[int],
            ppid: List[int],
            kill: int) -> List[int]:
        T = defaultdict(list)
        for child, parent in zip(pid, ppid):
            if parent != 0:
                T[parent].append(child)

        seen = set()
        self.ans = []

        def dfs(i):
            self.ans.append(i)
            for j in T[i]:
                if j not in seen:
                    seen.add(i)
                    dfs(j)

        dfs(kill)
        return self.ans


class Solution:
    def killProcess(
            self,
            pid: List[int],
            ppid: List[int],
            kill: int) -> List[int]:
        G = defaultdict(list)
        for c, p in zip(pid, ppid):
            G[p].append(c)

        ans = [kill]

        def dfs(node, iskill):
            if node == kill:
                iskill = True
            for c in G[node]:
                if iskill:
                    ans.append(c)
                dfs(c, iskill)

        dfs(0, False)
        return ans
