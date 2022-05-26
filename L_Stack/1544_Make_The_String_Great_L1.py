class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if not stk:
                stk.append(c)
            elif c.isupper() and stk[-1]==c.lower():
                stk.pop()
            elif c.islower() and stk[-1]==c.upper():
                stk.pop()
            else:
                stk.append(c)
        
        return ''.join(stk)
    
# trivial different solution with same idea
class Solution:
    def makeGood(self, S: str) -> str:
        s = []
        for c in S:
            r = 0
            if s and (chr(ord(c)+32)==s[-1] or chr(ord(c)-32)==s[-1]):
                s.pop()
                r = 1
            if not r: s.append(c)
            # print(s)
        return ''.join(s)