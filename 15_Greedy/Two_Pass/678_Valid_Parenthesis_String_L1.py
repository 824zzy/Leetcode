""" https://leetcode.com/problems/valid-parenthesis-string/
calculate balance parenthesis by left2right and right2left pass.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        bal_l, bal_r = 0, 0
        for i in range(len(s)):
            if s[i]=='*' or s[i]=='(': bal_l += 1
            elif s[i]==')': bal_l -= 1
            
            if s[~i]=='*' or s[~i]==')': bal_r += 1
            elif s[~i]=='(': bal_r -= 1
                
            if bal_l<0 or bal_r<0: return False
            
        return True