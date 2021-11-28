""" L1: Trie search by hash table
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        D = defaultdict(list)
        for w in words: D[w[0]].append(w)
        for c in s:
            W = D[c]
            D[c] = []
            for w in W:
                if len(w)>1: D[w[1]].append(w[1:])
                else: ans += 1
        return ans