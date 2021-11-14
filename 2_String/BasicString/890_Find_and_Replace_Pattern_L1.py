""" String preprocessing
Either caculate frequency or character replacement
"""
# calculate frequency
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            freq, f = [], {}
            for c in word:
                if c not in f: f[c] = len(f)
                freq.append(f[c])
            return freq
        
        p = convert(pattern)
        ans = []
        for w in words:
            if convert(w)==p: ans.append(w)
        return ans

# character replacement
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            base = 42
            for c in word:
                word = word.replace(c, chr(base))
                base += 1
            return word
        
        ans = []
        pattern = convert(pattern)
        for w in words:
            if convert(w)==pattern:
                ans.append(w)
        return ans