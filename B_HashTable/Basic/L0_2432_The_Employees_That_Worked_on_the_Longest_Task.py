""" https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
use hash table to store the task durations and employees
"""


class Solution:
    def hardestWorker(self, n: int, A: List[List[int]]) -> int:
        A = [[None, 0]] + A
        ans = defaultdict(list)
        for i in range(1, len(A)):
            ans[A[i][1] - A[i - 1][1]].append(A[i][0])
        return min(ans[max(ans)])


""" 1 3 0 12 1
10
[[0,3],[2,5],[0,9],[1,15]]
26
[[1,1],[3,7],[2,12],[7,17]]
2
[[0,10],[1,20]]
70
[[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]
10
[[0,3],[2,5],[0,9],[1,15]]
"""
