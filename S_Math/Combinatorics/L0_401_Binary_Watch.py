""" https://leetcode.com/problems/binary-watch/
use combinations to find all possible time
"""


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        H = [1, 2, 4, 8]
        M = [1, 2, 4, 8, 16, 32]
        ans = []
        for i in range(turnedOn + 1):
            h = list(combinations(H, i))
            m = list(combinations(M, turnedOn - i))
            for hh in h:
                for mm in m:
                    if sum(hh) < 12 and sum(mm) < 60:
                        ans.append(":".join([str(sum(hh)), str(sum(mm)).zfill(2)]))
        return ans
