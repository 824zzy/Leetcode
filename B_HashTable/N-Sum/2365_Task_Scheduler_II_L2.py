""" https://leetcode.com/problems/task-scheduler-ii/
also a n-sum problem as 2364_Count_Number_of_Bad_Pairs_L0.py
"""
class Solution:
    def taskSchedulerII(self, A: List[int], n: int) -> int:
        n += 1
        seen = defaultdict(lambda: -inf)
        ans = 0
        for x in A:
            ans = max(ans+1, seen[x]+n)
            seen[x] = ans
        return ans