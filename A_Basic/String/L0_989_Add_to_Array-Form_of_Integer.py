""" https://leetcode.com/problems/add-to-array-form-of-integer/
simulation
"""
class Solution:
    def addToArrayForm(self, A: List[int], k: int) -> List[int]:
        x = int(''.join(map(str, A)))
        return list(map(int, str(x+k)))
        