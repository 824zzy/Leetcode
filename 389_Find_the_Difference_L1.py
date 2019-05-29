
""" straightforward method using Counter
"""
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = dict(Counter(s))
        ct = dict(Counter(t))
        words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # print(cs, ct)
        for word in words:
            if word in cs and word in ct:
                if cs[word] != ct[word]:
                    return word
            elif word in cs or word in ct:
                return word
        
        