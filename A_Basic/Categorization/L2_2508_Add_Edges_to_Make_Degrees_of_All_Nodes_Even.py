""" https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/
The answer is constructed by three cases:
denote the node whose degree is odd as m
1. m=0: return True
2. m=2: directly connect the two nodes or enumerate 1~n to check if two edges is available to connect the three nodes
3. m=4: there are three ways to connect the four nodes
"""


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        odd = [k for k, v in G.items() if len(v) & 1]
        if len(odd) == 0:
            return True
        elif len(odd) == 2:
            x, y = odd
            if x not in G[y]:
                return True
            for i in range(1, n + 1):
                if i != x and i != y and x not in G[i] and y not in G[i]:
                    return True
            return False
        elif len(odd) == 4:
            a, b, c, d = odd
            return (
                b not in G[a]
                and c not in G[d]
                or c not in G[a]
                and b not in G[d]
                or d not in G[a]
                and c not in G[b]
            )
        else:
            return False
