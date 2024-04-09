""" https://leetcode.com/problems/reorder-data-in-log-files/
1. divide logs into L(letter-log) and D(digit-log)
2. sort L by content and identifier
3. combine them together
"""
from header import *


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        L, D = defaultdict(list), []
        for log in logs:
            identifier, content = log.split(' ', 1)
            if not content[0].isnumeric():
                L[content].append(identifier)
            else:
                D.append(log)

        _L = []
        for k, v in sorted(L.items()):
            for vv in sorted(v):
                _L.append(' '.join([vv] + [k]))
        return _L + D
