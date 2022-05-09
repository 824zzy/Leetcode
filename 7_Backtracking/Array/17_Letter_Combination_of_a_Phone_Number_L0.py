""" https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/445658/Python3-multiple-implementations-(96.33)
"""
class Solution:
    def letterCombinations(self, A: str) -> List[str]:
        mp = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']}
        ans = []
        stk = []
        
        def dfs(i):
            if i==len(A): 
                if stk: return ans.append(''.join(stk.copy()))
                else: return
                
            for c in mp[A[i]]:
                stk.append(c)
                dfs(i+1)
                stk.pop()
        
        dfs(0)
        return ans