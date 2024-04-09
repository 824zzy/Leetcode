""" https://leetcode.com/problems/encode-and-decode-strings/
1. Chunked transfer encoding, form the string by length of each string and the string itself.
2. use two pointers to decode the string
"""
from header import *


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ''
        for s in strs:
            ans += str(len(s)) + '|' + s
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        j = 0
        while j < len(s):
            while s[j] != '|':
                j += 1
            l = int(s[i:j])
            ans.append(s[j + 1:j + l + 1])
            j += l + 1
            i = j
        return ans

# cheating by special splitter


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        splitter = '!#$%^&*()'
        return splitter.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('!#$%^&*()')


"""
["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
"""
