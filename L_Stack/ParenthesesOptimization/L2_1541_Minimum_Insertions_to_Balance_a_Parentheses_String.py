""" https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
steal from: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/784514/Python3-easy-and-concise
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        ans = op = cl = 0  # open & closed parentheses
        i = 0
        while i <= len(s):
            if i == len(s) or s[i] == "(":
                if cl:
                    ans += 1  # add an extra closing parenthesis
                    if op:
                        op -= 1
                    else:
                        ans += 1  # add an opening parenthesis
                    cl = 0
                if i < len(s):
                    op += 1
            else:
                cl += 1
                if cl == 2:
                    if op:
                        op -= 1
                    else:
                        ans += 1  # add an opening parenthesis
                    cl = 0
            i += 1
        return ans + op * 2
