""" https://leetcode.com/problems/word-ladder-ii/
extension of 127
1. build graph of words
2. bfs to find ladder, note that use hash table to save paths and update visited words level-by-level
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    A: List[str]) -> List[List[str]]:
        # build graph of words
        G = defaultdict(list)
        for w in A:
            for i in range(len(w)):
                G[w[:i] + '*' + w[i + 1:]].append(w)
        # bfs to find ladder
        ans = []
        Q = {beginWord: [[beginWord]]}
        seen = {beginWord}
        while Q and not ans:
            nextQ = defaultdict(list)
            for w1, seqs in Q.items():
                for i in range(len(w1)):
                    for w2 in G[w1[:i] + '*' + w1[i + 1:]]:
                        if w2 == endWord:
                            ans.extend([seq + [w2] for seq in seqs])
                        if w2 not in seen:
                            for l in seqs:
                                nextQ[w2].append(l + [w2])
            # has to be updated level-by-level
            seen |= set(nextQ.keys())
            Q = nextQ
        return ans
