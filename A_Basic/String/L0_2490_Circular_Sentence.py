""" https://leetcode.com/problems/circular-sentence/description/
add the first word to the end of the sentence to make it circular
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        A = sentence.split()
        A = A + [A[0]]
        for i in range(len(A) - 1):
            if A[i][-1] != A[i + 1][0]:
                return False
        return True
