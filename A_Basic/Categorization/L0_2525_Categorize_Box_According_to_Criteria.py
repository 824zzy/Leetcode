""" https://leetcode.com/problems/categorize-box-according-to-criteria/
construct answer by criteria
"""


class Solution:
    def categorizeBox(self, l: int, w: int, h: int, mass: int) -> str:
        is_heavy = mass >= 100
        is_bulky = l >= 10**4 or w >= 10**4 or h >= 10**4 or (
            l * w * h) >= 10**9

        if is_heavy and is_bulky:
            return 'Both'
        elif not is_heavy and not is_bulky:
            return 'Neither'
        elif is_heavy:
            return 'Heavy'
        else:
            return 'Bulky'


"""
1000
35
700
300
200
50
800
50
2909
3968
3272
727
"""
