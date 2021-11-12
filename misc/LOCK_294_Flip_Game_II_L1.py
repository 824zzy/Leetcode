""" Simulate the game
"""
class Solution:
    def canWin(s: str) -> bool:
        if not s or len(s)<2:
            return False
        
        for i in range(len(s)):
            if s[i]=='+' and s[i+1]=='+':
                next_s = s[:i] + '--' + s[i+2:]
                if not canWin(next_s):
                    return True
        return False