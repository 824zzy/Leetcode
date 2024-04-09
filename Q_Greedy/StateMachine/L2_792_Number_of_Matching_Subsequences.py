""" https://leetcode.com/problems/number-of-matching-subsequences/
build state machine for the string, then check if the word is in the state machine.

Time complexity: O(T), where T is the sum of word length
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        s = '#' + s
        states = [[-1 for _ in range(26)] for _ in range(n + 1)]
        for i in reversed(range(1, n + 1)):
            for j in range(26):
                states[i - 1][j] = states[i][j]
            states[i - 1][ord(s[i]) - 97] = i

        ans = 0
        for w in words:
            i = 0
            for c in w:
                i = states[i][ord(c) - 97]
                if i == -1:
                    break
            else:
                ans += 1
        return ans
