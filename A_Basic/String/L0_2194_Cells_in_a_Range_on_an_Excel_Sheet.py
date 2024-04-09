""" https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
two loops for char columns and int rows
"""


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r0, r1 = int(s[1]), int(s[-1])
        c0, c1 = s[0], s[3]
        ans = []

        for i in range(ord(c0), ord(c1) + 1):
            for j in range(r0, r1 + 1):
                ans.append(chr(i) + str(j))
        return ans
