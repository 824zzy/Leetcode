""" https://leetcode.com/problems/find-and-replace-pattern
"""
class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        ans = []
        for word in words:
            if len(word)==len(p) and len(set(p))==len(set(word))==len(set(zip(word, p))):
                ans.append(word)
        return ans