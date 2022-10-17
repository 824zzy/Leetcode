""" https://leetcode.com/problems/number-of-valid-clock-times/
find rules for pattern matching
"""
class Solution:
    def countTime(self, T: str) -> int:
        H, M = T[:2], T[3:]
        
        if H=='??':
            h = 24
        elif H[0]=='?':
            if int(H[1])<4:
                h = 3
            else:
                h = 2
        elif H[1]=='?':
            if int(H[0])<2:
                h = 10
            else:
                h = 4
        else: 
            h = 1
            
        if M=='??':
            m = 60
        elif M[0]=='?':
            m = 6
        elif M[1]=='?':
            m = 10
        else:
            m = 1
        return m*h
            
        
"""
"?5:00"
"0?:0?"
"??:??"
"?1:?0"
"?4:22"
"""       
        
        
        