""" https://leetcode.com/problems/decode-the-message/
1. build a mapping from key to character
2. decode the message based on the mapping
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {}
        i = 0
        for c in key:
            if c.isalpha() and c not in mp:
                mp[c] = chr(i + ord('a'))
                i += 1

        ans = ''
        for c in message:
            if c.isalpha():
                ans += mp[c]
            else:
                ans += c
        return ans
