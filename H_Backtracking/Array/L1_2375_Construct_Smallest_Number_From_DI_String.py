""" https://leetcode.com/problems/construct-smallest-number-from-di-string/
using back-tracking to brute-force search the answer, which is suboptimal
for optimal solution see: /Q_Greedy/AdvanceGreedy/2375_Construct_Smallest_Number_From_DI_String_L3.py

Time complexity: O(2^n)
"""
class Solution:
    def smallestNumber(self, A: str) -> str:
        self.ans = '999999999'
        stk = []

        def dfs(i, prev):
            if i==len(A):
                self.ans = min(self.ans, ''.join(list(map(str, stk))))
                return
            for x in range(1, 10):
                if not prev:
                    stk.append(x)
                    dfs(i+1, x)
                    stk.pop()
                else:
                    if ((A[i]=='I' and x>prev) or (A[i]=='D' and x<prev)) and x not in stk:
                        stk.append(x)
                        dfs(i+1, x)
                        stk.pop()
                        
        dfs(-1, None)
        return self.ans