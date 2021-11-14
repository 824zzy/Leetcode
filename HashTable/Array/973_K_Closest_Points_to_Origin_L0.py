from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        coor = defaultdict(list)
        for i in points:
            coor[i[0]**2+i[1]**2].append(i)
        sortCoor = sorted(coor.items(), key=lambda x: x[0])
        ans, cur = [], 0
        while K:
            while sortCoor[cur][1] and K:
                ans.append(sortCoor[cur][1].pop())
                K -= 1
            cur += 1
        return ans