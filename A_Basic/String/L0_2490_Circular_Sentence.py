""" https://leetcode.com/problems/circular-sentence/description/
add the first word to the end of the sentence to make it circular
"""

from header import *


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        sentence += [sentence[0]]
        for x, y in pairwise(sentence):
            if x[-1] != y[0]:
                return False
        return True
