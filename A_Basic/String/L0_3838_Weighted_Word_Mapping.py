""" https://leetcode.com/problems/weighted-word-mapping/
For each word, sum character weights, take mod 26, and map to reverse alphabet
(0->'z', 1->'y', ..., 25->'a'). Concatenate all mapped characters.
"""


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letters = string.ascii_lowercase
        weights = {letters[i]: weights[i] for i in range(26)}
        ans = ""
        for w in words:
            sm = sum(weights[c] for c in w) % 26
            ans += letters[25 - sm]
        return ans
