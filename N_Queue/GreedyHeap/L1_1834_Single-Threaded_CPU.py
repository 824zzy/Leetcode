""" https://leetcode.com/problems/single-threaded-cpu/
1: [1,2]
3: [3,2], [2,4]
5: [4,1], [2,4]
"""
from header import *

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(t1, t2, i) for i, (t1, t2) in enumerate(tasks)]
        tasks.sort()
        pq = []
        t = 0
        ans = []
        
        for i in range(len(tasks)):
            while pq and tasks[i][0]>t:
                _t2, _i = heappop(pq)
                t += _t2
                ans.append(_i)
            # update cpu time
            t = max(t, tasks[i][0])
            heappush(pq, (tasks[i][1], tasks[i][2]))
        
        while pq:
            ans.append(heappop(pq)[1])
        return ans
                
        
        
"""
[[1,2],[2,4],[3,2],[4,1]]
[[7,10],[7,12],[7,5],[7,4],[7,2]]
[[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]
[[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
"""