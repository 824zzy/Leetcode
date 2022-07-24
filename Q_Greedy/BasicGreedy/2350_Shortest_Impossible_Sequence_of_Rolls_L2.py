""" https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
greedily check the first occurrence of all number from 1 to k.
Once find all the numbers, reset the seen set to empty.
"""
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 1
        for x in rolls:
            seen.add(x)
            if len(seen)==k:
                ans += 1
                seen = set()
        return ans