""" https://leetcode.com/problems/k-similar-strings/
TODO:
"""


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        Q = [s1]
        seen = {s1}
        res = 0

        while Q:
            # print(Q)
            nxtQ = []
            for s in Q:
                if s == s2:
                    return res
                for i in range(len(s)):
                    if s[i] != s2[i]:
                        for j in range(i + 1, len(s)):
                            if s[j] != s2[j] and s[j] == s2[i]:
                                # swap
                                ss = s[:i] + s[j] + s[i + 1 : j] + s[i] + s[j + 1 :]
                                if ss not in seen:
                                    seen.add(ss)
                                    nxtQ.append(ss)
                        break
            res += 1
            Q = nxtQ
