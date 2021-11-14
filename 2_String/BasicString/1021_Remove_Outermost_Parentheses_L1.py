""" use cnt to find valid parentheses
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt, ans, tmp = 0, '', []
        for s in S:
            if s=='(': cnt += 1
            else: cnt -= 1
            tmp.append(s)
            if cnt==0:
                ans += ''.join(tmp[1:-1])
                tmp = []
        return ans