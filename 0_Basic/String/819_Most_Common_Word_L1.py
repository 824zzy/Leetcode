""" Amazon
string.punctuation
"""
from string import punctuation
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        P = [c.lower() if c not in punctuation else ' ' for c in paragraph]
        alter = ''.join(P).split()
        alter = [a for a in alter if a not in banned]
        counter = Counter(alter)
        return counter.most_common(1)[0][0]