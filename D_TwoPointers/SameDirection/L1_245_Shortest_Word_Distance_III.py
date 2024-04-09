""" https://leetcode.com/problems/shortest-word-distance-iii/
two cases:
1. word1==word2, use a flag to indicate whether the last word is word1 or not
2. word1!=word2, use two pointers to record the last index of word1 and word2
"""
from header import *


class Solution:
    def shortestWordDistance(
            self,
            wordsDict: List[str],
            word1: str,
            word2: str) -> int:
        ans = inf
        i, j = inf, inf
        if word1 == word2:
            f = True
            for idx, w in enumerate(wordsDict):
                if w == word1:
                    if f:
                        i = idx
                        f = False
                    else:
                        j = idx
                        f = True
                ans = min(ans, abs(i - j))
        else:
            for idx, w in enumerate(wordsDict):
                if w == word1:
                    i = idx
                elif w == word2:
                    j = idx
                ans = min(ans, abs(i - j))
        return ans


"""
["practice", "makes", "perfect", "coding", "makes"]
"makes"
"coding"
["practice", "makes", "perfect", "coding", "makes"]
"makes"
"makes"
"""
