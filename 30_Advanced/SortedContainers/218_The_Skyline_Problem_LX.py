""" https://leetcode.com/problems/the-skyline-problem/
TODO: https://leetcode.com/problems/the-skyline-problem/discuss/812312/Python-Sweep-Line-%2B-SortedList-or-O(nlogn)
"""
import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # to be a skyline point either:
        # 1. entering event with highest height
        # 2. leaving event with highest height
        # to handle edge case
        # sort the entering event by increasing order of height
        # sort the leaving event by decreasing order of height
        events = [[x, b[2], enter] for b in buildings for x, enter in zip(b[:2], [1, -1])]
        events.sort(key=lambda x: (x[0], -x[1]*x[2]))
        ans = []
        # heights so far
        heights = sortedcontainers.SortedList()
        for i, event in enumerate(events):
            x, h, status = event[0], event[1], event[2]
            if status == 1:
                if not heights or h > heights[-1]:
                    ans.append([x,h])
                heights.add(h)
            else:
                heights.discard(h)
                if not heights:
                    ans.append([x, 0])
                elif h > heights[-1]:
                    ans.append([x, heights[-1]])
        return ans