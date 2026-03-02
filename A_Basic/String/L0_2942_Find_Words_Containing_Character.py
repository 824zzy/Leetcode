""" https://leetcode.com/problems/find-words-containing-character/
string simulation
"""


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
