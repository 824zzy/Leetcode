""" https://leetcode.com/problems/find-common-characters/
use Counter intersection operation
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = Counter(A[0])
        for x in A:
            ans &= Counter(x)
        return list(ans.elements())