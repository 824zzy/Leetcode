""" https://leetcode.com/problems/word-pattern-ii/
backtracking with two hash table
"""


class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        p2s = {}
        s2p = {}

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            elif i == len(s) or j == len(p):
                return False
            ans = False
            for k in range(i, len(s)):
                if p[j] not in p2s and s[i : k + 1] not in s2p:
                    p2s[p[j]] = s[i : k + 1]
                    s2p[s[i : k + 1]] = p[j]
                    ans |= dfs(k + 1, j + 1)
                    p2s.pop(p[j])
                    s2p.pop(s[i : k + 1])
                elif (
                    p2s.get(p[j], "") == s[i : k + 1]
                    and s2p.get(s[i : k + 1], "") == p[j]
                ):
                    ans |= dfs(k + 1, j + 1)
            return ans

        return dfs(0, 0)


"""
"abab"
"redblueredblue"
"aaaa"
"asdasdasdasd"
"aabb"
"xyzabcxzyabc"
"ab"
"aa"
"""
