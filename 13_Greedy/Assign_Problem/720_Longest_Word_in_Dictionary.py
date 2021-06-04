""" L1: sort words and check
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        seen = set()
        ans = ''
        seen.add('')
        for word in words:
            if word[:-1] in seen:
                if len(word)>len(ans):
                    ans = word
                seen.add(word)
        return ans