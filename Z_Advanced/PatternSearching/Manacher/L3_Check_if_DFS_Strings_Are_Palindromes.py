""" https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
timestamp dfs + Manacher
"""

from header import *


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        G = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            G[p].append(i)

        dfsStr = [""] * n
        nodes = [[0, 0] for _ in range(n)]
        time = 0

        def dfs(x):
            # timestamp dfs
            nonlocal time
            nodes[x][0] = time
            for y in G[x]:
                dfs(y)
            dfsStr[time] = s[x]
            time += 1
            nodes[x][1] = time

        dfs(0)

        # Manacher template
        t = "#".join(["^"] + dfsStr + ["$"])
        half_len = [0] * (len(t) - 2)
        half_len[1] = 1
        box_m = box_r = 0
        for i in range(2, len(half_len)):
            hl = 1
            if i < box_r:
                hl = min(half_len[box_m * 2 - i], box_r - i)

            while t[i - hl] == t[i + hl]:
                hl += 1
                box_m, box_r = i, i + hl

            half_len[i] = hl

        def isPalindrome(l, r):
            return half_len[l + r + 1] > r - l

        return [isPalindrome(l, r) for l, r in nodes]
