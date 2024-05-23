""" https://leetcode.com/problems/palindrome-partitioning/
since s.length<=16, just backtracking is enough

There are two ways of backtracking:
1. use for loop to iterate all possible cut points
2. knapsack style, use a helper function to check if the current string is palindrome
"""
from header import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        stk = []

        def dfs(i):
            if i == len(s):
                return ans.append(stk.copy())
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    stk.append(s[i:j])
                    dfs(j)
                    stk.pop()
        dfs(0)
        return ans


class Solution:
    def partition(self, A: str) -> List[List[str]]:
        def check(s):
            if not s:
                return False
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = []
        stk = []

        def dfs(i, s):
            if i == len(A):
                if check(s):
                    stk.append(s)
                    ans.append(stk.copy())
                    stk.pop()
                return
            # cut if s is palindrome
            if s and check(s):
                stk.append(s)
                dfs(i+1, A[i])
                stk.pop()
            # don't cut
            dfs(i+1, s+A[i])

        dfs(0, '')
        return ans
