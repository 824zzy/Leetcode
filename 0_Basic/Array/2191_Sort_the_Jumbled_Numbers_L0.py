""" https://leetcode.com/problems/sort-the-jumbled-numbers/
liner scan based on mapping and sort
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mp = {str(i): str(x) for i, x in enumerate(mapping)}
        A = []
        for i, x in enumerate(nums):
            A.append([int(''.join(mp[c] for c in str(x))), i, x])
        A.sort()
        return [x for v, i, x in A]