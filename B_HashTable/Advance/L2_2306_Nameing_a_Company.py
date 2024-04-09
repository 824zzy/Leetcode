""" https://leetcode.com/problems/naming-a-company/
from lee: https://leetcode.com/problems/naming-a-company/discuss/2141172/JavaC%2B%2BPython-Group-by-First-Letter

Any idea = first letter + postfix string.
We can group all ideas by their first letter.

If two ideas ideas[i] and ideas[j] share a common postfix string,
then ideas[i] can not pair with any idea starts with ideas[j][0]
and ideas[j] can not pair with any idea starts with ideas[i][0].
"""
from header import *


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        mp = defaultdict(set)
        for x in ideas:
            mp[x[0]].add(x[1:])

        ans = 0
        for _, x in mp.items():
            for _, y in mp.items():
                same = len(x & y)
                ans += (len(x) - same) * (len(y) - same)
        return ans

# another implementation


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Group strings by their initials
        mp = defaultdict(set)
        for x in ideas:
            mp[ord(x[0]) - 97].add(x[1:])

        ans = 0
        # Calculate number of valid names from every initial pair.
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(mp[i] & mp[j])
                ans += 2 * (len(mp[i]) - k) * (len(mp[j]) - k)
        return ans
