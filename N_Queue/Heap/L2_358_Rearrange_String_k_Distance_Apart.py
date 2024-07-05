""" https://leetcode.com/problems/rearrange-string-k-distance-apart/
greedy heap simulation, using busy to store the busy time of each char.
"""
from header import *


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        cnt = Counter(s)
        free = [(-b, a) for a, b in cnt.items()]
        heapify(free)
        busy = []
        ans = []
        while len(ans) != len(s):
            index = len(ans)
            if busy and index - busy[0][0] >= k:
                _, ff, cc = busy.pop(0)
                heappush(free, (ff, cc))
            if len(free) == 0:
                return ""
            f, c = heappop(free)
            ans.append(c)
            if f + 1 < 0:
                busy.append((index, f + 1, c))
        return "".join(ans)


"""
"aabbcc"
3
"aaabc"
3
"aaadbbcc"
2
"""
