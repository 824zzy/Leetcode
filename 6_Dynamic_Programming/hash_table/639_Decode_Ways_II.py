""" L2
dp['0'] = current number of ways we could decode, ending on any number;
dp['1'] = current number of ways we could decode, ending on an open 1;
dp['2'] = current number of ways we could decode, ending on an open 2;

If c == '*', then the number of ways to finish in total is: we could put * as a single digit number (9*e0), 
or we could pair * as a 2 digit number 1* in 9*e1 ways, or we could pair * as a 2 digit number 2* in 6*e2 ways. 
The number of ways to finish with an open 1 (or 2) is just e0.

If c != '*', then the number of ways to finish in total is: we could put c as a single digit if it is not zero 
((c>'0')*e0), or we could pair c with our open 1, or we could pair c with our open 2 if it is 6 or less 
((c<='6')*e2). The number of ways to finish with an open 1 (or 2) is e0 iff c == '1' (or c == '2').
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9+7
        dp = {'0': 1, '1':0, '2': 0}
        for c in s:
            if c=='*':
                f0 = 9*dp['0']+9*dp['1']+6*dp['2']
                f1 = dp['0']
                f2 = dp['0']
            else:
                f0 = (c>'0')*dp['0']+dp['1']+(c<='6')*dp['2']
                f1 = (c=='1')*dp['0']
                f2 = (c=='2')*dp['0']
            dp['0'], dp['1'], dp['2'] = f0%MOD, f1, f2
        return dp['0']