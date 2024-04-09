""" https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')\
             .replace('XL', 'XXXX').replace('XC', 'LXXXX')\
             .replace('CD', 'CCCC').replace('CM', 'DCCCC')
        return sum([m[c] for c in s])


class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        ans = 0
        i = 0
        while i < len(s):
            if s[i:i + 2] in mp:
                ans += mp[s[i:i + 2]]
                i += 2
            else:
                ans += mp[s[i:i + 1]]
                i += 1
        return ans
