""" https://leetcode.com/problems/rearrange-spaces-between-words/
count spaces, divmod to distribute evenly, remainder appended at end
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * spaces
        gap, extra = divmod(spaces, len(words) - 1)
        return (' ' * gap).join(words) + ' ' * extra
