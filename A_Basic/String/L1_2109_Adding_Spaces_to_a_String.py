""" https://leetcode.com/problems/adding-spaces-to-a-string/
read from backward and add spaces
"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        for i in reversed(range(len(s))):
            ans.append(s[i])
            if spaces and i == spaces[-1]:
                ans.append(" ")
                spaces.pop()
        return "".join(ans[::-1])


# or simply create such a string by indices


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces
        parts = [s[i:j] for i, j in zip(spaces, spaces[1:] + [None])]
        return " ".join(parts)
