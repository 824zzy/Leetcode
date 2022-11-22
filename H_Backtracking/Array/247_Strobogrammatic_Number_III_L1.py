""" https://leetcode.com/problems/strobogrammatic-number-ii/
Similar to 247.
"""
from header import *

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mp = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',            
        }
        stk = []
        self.ans = 0

        def dfs(i):
            if i>len(high)//2+1: return
            if len(low)//2<=i<=len(high)//2:
                for c in '018':
                    s = str(int(''.join(stk+[c]+[mp[x] for x in stk][::-1])))
                    if stk and stk[0]=='0': continue
                    if int(low)<=int(s)<=int(high):
                        self.ans += 1                            
                if stk:
                    s = str(int(''.join(stk+[mp[x] for x in stk][::-1])))
                    if stk[0]!='0' and int(low)<=int(s)<=int(high):
                        self.ans += 1

            for c in mp:
                stk.append(c)
                dfs(i+1)
                stk.pop()
        dfs(0)
        return self.ans