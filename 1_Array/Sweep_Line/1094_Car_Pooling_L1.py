from collections import defaultdict, Counter
class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        n = max([t[2] for t in trips])
        count = [0] * (n + 1)
        for t, i, j in trips:
            count[i-1] += t
            count[j-1] -= t
        for i in range(1, n+1):
            count[i] += count[i - 1]

        for c in count:
            if c>cap:
                return False
        return True
    
# Naive solution
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cnt = Counter()
        for t in trips:
            for i in range(t[1], t[2]):
                cnt[i] += t[0]
        return all([v<=capacity for v in cnt.values()])