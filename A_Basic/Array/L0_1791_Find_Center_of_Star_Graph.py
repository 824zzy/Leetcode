"""
only need to compare edges[0] and edges[1]
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = Counter(edges[0] + edges[1])
        for k, v in cnt.items():
            if v == 2:
                return k


class Solution:
    def findCenter(self, e):
        return (set(e[0]) & set(e[1])).pop()
