""" L0: https://leetcode.com/problems/plus-one/submissions/
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(map(str, digits))) + 1
        return [int(x) for x in str(n)]
