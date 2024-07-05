""" https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/
1. find left most non 'a' char
2. start from that char, replace all non 'a' char with (non 'a'-1)
"""


class Solution:
    def smallestString(self, s: str) -> str:
        S = list(s)
        for i, c in enumerate(S):
            if c != "a":
                for j in range(i, len(S)):
                    if S[j] == "a":
                        break
                    S[j] = chr(ord(S[j]) - 1)
                return "".join(S)
        S[-1] = "z"
        return "".join(S)
