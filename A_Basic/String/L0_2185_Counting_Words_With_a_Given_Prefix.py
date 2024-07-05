""" https://leetcode.com/problems/counting-words-with-a-given-prefix/
use startswith or string slicing.
"""


class Solution:
    def prefixCount(self, A: List[str], pref: str) -> int:
        return sum([x.startswith(pref) for x in A])


class Solution:
    def prefixCount(self, A: List[str], pref: str) -> int:
        return sum([1 for x in A if x[: len(pref)] == pref])
