""" https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
This problem is easy because the data size is very small, state machine is the optimal solution for this problem.

1. sort string by length and lexicographical order
2. compare characters by two pointers

Time complexity: O(m*n), where m is the length of string and n is the length of dictionary
"""


class Solution:
    def findLongestWord(self, s: str, D: List[str]) -> str:
        D = sorted(D, key=lambda x: (-len(x), x))
        for w in D:
            i = 0
            for j in range(len(s)):
                if w[i] == s[j]:
                    i += 1
                if i == len(w):
                    return w
        return ""
