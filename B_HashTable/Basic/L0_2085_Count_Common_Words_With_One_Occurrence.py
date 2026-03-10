""" https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""


class Solution:
    def countWords(self, W1: List[str], W2: List[str]) -> int:
        A = [k for k, v in Counter(W1).items() if v == 1]
        B = [k for k, v in Counter(W2).items() if v == 1]
        return sum([1 for a in A if a in B])
