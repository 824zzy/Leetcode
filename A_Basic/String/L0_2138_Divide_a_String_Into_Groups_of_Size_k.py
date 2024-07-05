""" https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
simulation
"""


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i : i + k])
        if len(ans[-1]) < k:
            ans[-1] = ans[-1] + (k - len(ans[-1])) * fill
        return ans
