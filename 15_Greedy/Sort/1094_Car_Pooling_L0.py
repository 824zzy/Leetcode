from collections import defaultdict, Counter
class Solution:
    def carPooling(self, trips: List[List[int]], c: int) -> bool:
        n2s = defaultdict(list)
        n2e = defaultdict(list)
        trips = sorted(trips, key=lambda x: x[1])
        for i, s, e in trips:
            n2s[s].append(i)
            n2e[e].append(i)
            
        th = c
        for i in range(1, n+1):
            if n2s[i]:
                c -= sum(n2s[i])
            if n2e[i]:
                c += sum(n2e[i])
            if c<0 or c>th:
                return False
        return True