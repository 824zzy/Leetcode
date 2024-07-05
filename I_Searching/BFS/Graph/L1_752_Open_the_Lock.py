""" https://leetcode.com/problems/open-the-lock/
1. Consider the problem as a graph problem, the goal is to find shortest way between two nodes.
2. Use bfs to find the shortest path.
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        Q = [("0000", 0)]
        seen = set(deadends)
        while Q:
            lock, step = Q.pop(0)
            if lock == target:
                return step
            for i in range(4):
                for d in (1, -1):
                    new = lock[:i] + str((int(lock[i]) + d) % 10) + lock[i + 1 :]
                    if new not in seen:
                        Q.append((new, step + 1))
                        seen.add(new)
        return -1
