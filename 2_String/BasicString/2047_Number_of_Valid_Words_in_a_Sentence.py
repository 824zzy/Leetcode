""" L1: https://leetcode.com/contest/weekly-contest-264/problems/number-of-valid-words-in-a-sentence/
disgust and gross
"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def check(word):
            seen = False
            for i, c in enumerate(word):
                if c.isdigit() or (c in "!.," and i!=len(word)-1): return False
                elif c=='-':
                    if seen or i==0 or i==len(word)-1 or not word[i+1].isalpha(): return False
                    seen = True
            return True
        
        return sum(check(word) for word in sentence.split())