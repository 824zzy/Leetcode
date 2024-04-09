""" https://leetcode.com/problems/maximum-number-of-words-you-can-type/
split text and check if all the broken words are not in the current word.
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for w in text.split():
            if all([l not in w for l in brokenLetters]):
                ans += 1
        return ans
