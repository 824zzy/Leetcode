""" https://leetcode.com/problems/valid-number/
string + categorization

simulation
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        def sanity_check(s):
            s = s.lower()
            for i in range(26):
                if i==4: continue # skip e
                if chr(i+97) in s:
                    return False
            return True
        
        def is_integer(s):
            if not s: return False
            if s[0] in '+-':
                s = s[1:]
            return s.isdigit()
        
        def is_decimal(s):
            if s[0] in '+-':
                s = s[1:]
            s = s.split('.')
            if len(s)>2: # edge case: '0..'
                return False
            elif s[0]=='': # case3: A dot '.', followed by one or more digits.
                return s[1].isdigit()
            else: # case 1 and 2
                return (s[0].isdigit() and s[1]=='') or (s[0].isdigit() and s[1].isdigit())
            
        # check if a-z except e in s
        if not sanity_check(s):
            return False
        # split by exponential
        if 'e' in s or 'E' in s:
            if 'e' in s:
                s = s.split('e')
            elif 'E' in s:
                s = s.split('E')
            # must split to one or two part
            if len(s)>2: 
                return False
            # check second is integer
            if not is_integer(s[1]):
                return False
            s = s[0]
        # check the first part: integer or decimal
        if '.' in s: # first part is decimal
            if not is_decimal(s):
                return False
        else: # first part is integer
            if not is_integer(s):
                return False
        return True
            
        
"""
"0"
"e"
"."
"2"
"0089"
"-0.1"
"+3.14"
"4."
"-.9"
"2e10"
"-90E3"
"3e+7"
"+6e-1"
"53.5e93"
"-123.456e789"
"abc"
"1a"
"1e"
"e3"
"99e2.5"
"--6"
"-+3"
"95a54e53"
"0.."
"+-."
".-4"
"""