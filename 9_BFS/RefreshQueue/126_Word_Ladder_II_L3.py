""" https://leetcode.com/problems/word-ladder-ii/
extension of 127

The problem is required to output the answer sequence paths, 
so we need to store sequences path so far while doing bfs.

Notice that we are removing words at each layer, this avoids using a visited set, further saving on time and space.
"""
class Solution:
    def findLadders(self, begin: str, end: str, A: List[str]) -> List[List[str]]:
        A = [begin] + A 
        G = defaultdict(set)
        setA = set(A)
        for w in A:
            for i in range(len(A[0])):
                p1, p2 = w[:i], w[i+1:]
                for j in range(26):
                    if p1+chr(ord('a')+j)+p2!= w and p1+chr(ord('a')+j)+p2 in setA:
                        G[w].add(p1+chr(ord('a')+j)+p2)
                        
        # bfs
        Q = {begin: [[begin]]}
        seen = {begin}
        ans = []
        while Q and not ans:
            nextQ = {}
            for i, paths in Q.items():
                for j in G[i]:
                    if j==end: ans.extend([p+[j] for p in paths])
                    if j not in seen:
                        for path in paths:
                            nextQ.setdefault(j, []).append(path+[j])
            seen |= set(nextQ.keys())
            Q = nextQ
        return ans