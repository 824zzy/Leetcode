class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        stk = []
        for i, c in enumerate(s):
            if c not in stk:
                while stk and c<stk[-1] and i<lastIdx[stk[-1]]:
                    stk.pop()
                stk.append(c)
        return ''.join(stk)