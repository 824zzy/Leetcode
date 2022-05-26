""" https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
1. use topological sort to iterate from leaves to root
2. maintain the top two longest paths of very nodes to record the global longest path.

Time: O(n)
"""
class Solution:
    def longestPath(self, P: List[int], s: str) -> int:
        G = defaultdict(list)
        inD = [0] * (len(P))
        for i, j in enumerate(P):
            if j>=0: 
                G[i].append(j)
                inD[j] += 1
        
        Q = [[i, 1] for i, d in enumerate(inD) if d==0]
        LP = [[0, 0] for _ in range(len(P))] # longest two paths of every nodes
        ans = 1
        while Q:
            i, l = Q.pop(0)
            for j in G[i]:
                inD[j] -= 1
                # if the child has different char with parent
                if s[i]!=s[j]:
                    # update gloabl longest paths
                    if l>LP[j][1]: LP[j][0], LP[j][1] = LP[j][1], l
                    elif l>LP[j][0]: LP[j][0] = l
                # add parent to queue
                if not inD[j]: 
                    ans = max(ans, 1+sum(LP[j]))
                    Q.append([j, 1+max(LP[j])])
        return ans