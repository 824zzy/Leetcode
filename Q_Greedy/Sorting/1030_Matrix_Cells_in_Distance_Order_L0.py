class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dist = collections.defaultdict(list)
        for i in range(R):
            for j in range(C):
                d = abs(i-r0)+abs(j-c0)
                dist[d].append([i, j])
        ans = []
        for k, v in sorted(dist.items()):
            ans.extend(v)
        return ans