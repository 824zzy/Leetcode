""" https://leetcode.com/problems/valid-word-abbreviation/
two pointers + categorization
"""


class Solution:
    def validWordAbbreviation(self, s: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(abbr):
            if abbr[j].isalpha():
                if s[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if abbr[j] == "0":
                    return False
                jj = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[jj:j])
        return i == len(s) and j == len(abbr)


# string construction and comparison


class Solution:
    def validWordAbbreviation(self, s: str, abbr: str) -> bool:
        i = 0
        n = 0
        for j in range(len(abbr)):
            if abbr[j].isalpha():
                if n:
                    i += n
                    n = 0
                if i < len(s) and s[i] != abbr[j]:
                    return False
                else:
                    i += 1
            elif abbr[j].isdigit():
                if n == 0 and abbr[j] == "0":
                    return False
                n = n * 10 + int(abbr[j])
        return (i + n) == len(s)


"""
"internationalization"
"i12iz4n"
"apple"
"a2e"
"a"
"1"
"a"
"0"
"ab"
"1"
"ab"
"b1"
"a"
"12"
"a"
"01"
"hi"
"1i"
"bignumberhahaha"
"999999999"
"""
