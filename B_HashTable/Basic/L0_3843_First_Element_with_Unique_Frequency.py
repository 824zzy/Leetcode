""" https://leetcode.com/problems/first-element-with-unique-frequency/
Two-layer Counter: cnt counts element frequencies, _cnt counts how many
elements share each frequency. Scan left to right, return the first element
whose frequency appears exactly once in _cnt.
"""


class Solution:
    def firstUniqueFreq(self, A: List[int]) -> int:
        cnt = Counter(A)
        _cnt = Counter(cnt.values())
        for x in A:
            if _cnt[cnt[x]] == 1:
                return x
        return -1
