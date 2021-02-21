class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        for i, c in enumerate(s):
            if not c.isalpha(): stk.append([c, i])
            while len(stk)>1 and stk[-1][0]==')':
                if stk[-2][0]=='(': 
                    stk.pop()
                    stk.pop()
                else: break
        s = list(s)
        for i in stk: s[i[1]] = '!'
        return ''.join(s).replace('!', '')