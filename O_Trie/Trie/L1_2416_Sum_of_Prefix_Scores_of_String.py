""" https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
prefix set trie or trie

TODO: solve it again
"""
from header import *


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix = defaultdict(int)
        for w in words:
            _p = ""
            for i in range(len(w)):
                _p += w[i]
                prefix[_p] += 1

        ans = []
        for w in words:
            curr = 0
            _p = ""
            for i in range(len(w)):
                _p += w[i]
                curr += prefix[_p]
            ans.append(curr)

        return ans


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
                node["#"] = node.get("#", 0) + 1

        ans = []
        for word in words:
            val = 0
            node = root
            for ch in word:
                node = node[ch]
                val += node["#"]
            ans.append(val)
        return ans
