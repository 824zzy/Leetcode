""" https://leetcode.com/problems/construct-smallest-number-from-di-string/
learn from lee, reverse all the numbers between the two 'I'
"""
class Solution:
    def smallestNumber(self, A: str) -> str:
        ans = []
        stk = []
        for i, c in enumerate(A+'I', 1):
            stk.append(str(i))
            if c=='I':
                ans += stk[::-1]
                stk = []
        return ''.join(ans)