""" https://leetcode.com/problems/concatenated-words/
Consider prefix set as a trie, we scan each word by length order 
then use dfs to check if the word can be concatenated by prefix set

Time complexity: O(n)
"""
from header import *

class Solution:
    def findAllConcatenatedWordsInADict(self, A: List[str]) -> List[str]:
        def dfs(x):
            if not x: return True
            ans = False
            for j in range(1, len(x)+1):
                if x[:j] in prefix:
                    ans |= dfs(x[j:])
            return ans
            
        A.sort(key=len)
        ans = []
        prefix = set()
        for x in A:
            if dfs(x):
                ans.append(x)
            prefix.add(x)
        return ans