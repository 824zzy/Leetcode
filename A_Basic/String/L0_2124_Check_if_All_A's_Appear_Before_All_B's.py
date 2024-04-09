""" https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
dumb solution: check orders by groupby
smart solution: check if 'ba' in s
"""


class Solution:
    def checkString(self, s: str) -> bool:
        s = [k for k, v in groupby(s)]
        if (len(s) <= 2 and s[0] == 'a') or (len(s) == 1 and s[0] == 'b'):
            return True
        else:
            return False


class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
