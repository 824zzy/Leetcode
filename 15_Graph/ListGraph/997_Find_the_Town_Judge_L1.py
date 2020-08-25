# List as graph
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1

        for i in range(1, N+1):
            if count[i]==N-1:
                return i
        return -1


# Dict graph pretty slow
from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            if N==1:
                return 1
            else:
                return -1
        g = defaultdict(list)
        for rel in trust:
            g[rel[1]].extend([rel[0]])
        
        possible_j = [k for k, v in g.items() if len(v)==N-1]
        if possible_j:
            possible_j = possible_j[0]
            trust = [k for k, v in g.items() if possible_j in v]
            if trust:
                return -1
            else:
                return possible_j
        else:
            return -1