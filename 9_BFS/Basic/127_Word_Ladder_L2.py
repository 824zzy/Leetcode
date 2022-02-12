""" https://leetcode.com/problems/word-ladder/
1. create a graph by checking all possible candidates O(n*len(w)*26) rather than double for loop O(n^2)
2. classic bfs to find minimum step
"""
class Solution:
    def ladderLength(self, begin: str, end: str, A: List[str]) -> int:
        # build graph O(n*len(w)*26)
        A = [begin] + A 
        G = defaultdict(list)
        setA = set(A)
        for w in A:
            for i in range(len(A[0])):
                p1, p2 = w[:i], w[i+1:]
                for j in range(26):
                    if p1+chr(ord('a')+j)+p2 in setA:
                        G[w].append(p1+chr(ord('a')+j)+p2)
        # bfs
        Q = [[begin, 1]]
        seen = set()
        seen.add(begin)
        while Q:
            i, step = Q.pop(0)
            if i==end: return step
            for j in G[i]:
                if j not in seen:
                    Q.append([j, step+1])
                    seen.add(j)
        return 0