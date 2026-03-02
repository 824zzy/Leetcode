""" https://leetcode.com/problems/sort-the-people/
zip two arrays and sort by people's height
"""


class Solution:
    def sortPeople(self, A: List[str], H: List[int]) -> List[str]:
        return [a for a, h in sorted(list(zip(A, H)), key=lambda x: -x[1])]
