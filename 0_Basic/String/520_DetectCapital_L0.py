""" https://leetcode.com/problems/detect-capital/
python string method usage
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.lower(), word.upper(), word.capitalize())