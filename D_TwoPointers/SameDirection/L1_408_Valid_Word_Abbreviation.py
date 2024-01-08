""" https://leetcode.com/problems/valid-word-abbreviation/
two pointers + simulation

very tricky problem
"""
class Solution:
    def validWordAbbreviation(self, s: str, abbr: str) -> bool:
        i, j = 0, 0
        while i<len(s) and j<len(abbr):
            if abbr[j].isalpha():
                if s[i]==abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if abbr[j]=='0':
                    return False
                jj = j
                while j<len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[jj:j])
        return i==len(s) and j==len(abbr)
            
# string construction and comparison
class Solution:
    def validWordAbbreviation(self, s: str, abbr: str) -> bool:
        D = "". join(["*" if not c.isdigit() else c for c in abbr]).replace("*", ' ').split()
        C = "". join(["*" if c.isdigit() else c for c in abbr]).replace("*", ' ').split()
        _s = ''
        if abbr[0].isdigit():
            while C or D:
                if D:
                    d = D.pop(0)
                    if d[0]=='0' or int(d)>20: return False
                    _s += "*"*(int(d))
                if C:
                    _s += C.pop(0)
        else:
            while C or D:
                if C:
                    _s += C.pop(0)
                if D:
                    d = D.pop(0)
                    if d[0]=='0' or int(d)>20: return False
                    _s += "*"*(int(d))
        if len(s)!=len(_s): return False
        for x, y in zip(s, _s):
            if y=="*": continue
            if x!=y: return False
        return True
                
                         
                
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