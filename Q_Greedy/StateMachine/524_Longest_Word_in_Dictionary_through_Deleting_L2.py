""" https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
This problem is easy because the data size is very small, state machine is the optimal solution for this problem.

1. sort string by length and lexicographical order 
2. compare characters by two pointers

Time complexity: O(m*n), where m is the length of string and n is the length of dictionary
"""
class Solution:
    def findLongestWord(self, s: str, D: List[str]) -> str:
        n = len(s)
        s = '#' + s
        states = [[-1 for _ in range(26)] for _ in range(n+1)]
        for i in reversed(range(1, n+1)):
            for j in range(26):
                states[i-1][j] = states[i][j]
            states[i-1][ord(s[i])-97] = i
        
        ans = 0
        for w in sorted(D, key=lambda x:(-len(x), x)):
            i = 0
            for c in w:
                i = states[i][ord(c)-97]
                if i==-1: break
            else: return w
        return ''