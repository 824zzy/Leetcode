""" L1: brain teaser
First, this is string rotation.
12345 -> 23451 -> 34512 -> 45123 -> 51234
I use number instead of letters to make it clear.

If K == 1, we can only rotate the whole string.
There are S.length different states and
we return the lexicographically smallest string.

If K > 1, it means we can:

rotate the whole string,
rotate the whole string except the first letter.
012345 -> 023451 -> 034512 -> 045123 -> 051234
We can rotate i+1th big letter to the start (method 1),
then rotate ith big letter to the end (method 2).
2XXX01 -> XXX012

In this way, we can bubble sort the whole string lexicographically.
So just return sorted string.
"""
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1: return "".join(sorted(s))
        cand = [s[i:]+s[:i] for i in range(len(s))]
        return min(cand)
