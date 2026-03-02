""" https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for k, v in Counter(S).items():
            if k in J:
                ans += v
        return ans
