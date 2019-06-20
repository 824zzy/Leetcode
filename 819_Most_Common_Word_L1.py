""" string.punctuation
"""
from string import punctuation
from collection import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = ""
        for c in paragraph:
            if c in punctuation:
                c = " "
                p += c
            else:
                p += c.lower()
        p = p.split()
        alter = [c for c in p.split() if c not in banned]
        
        counter = Counter(alter)
        return counter.most_common(1)[0][0]
        
        