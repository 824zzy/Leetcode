""" https://leetcode.com/problems/maximum-number-of-robots-within-budget/
binary search + monotonic queue

note that all the running cost is positive, so it is not necessary to use monotonic queue on runningCosts!
"""
from header import *


class Solution:
    def maximumRobots(self, A: List[int], C: List[int], b: int) -> int:
        C = list(accumulate(C, initial=0))
        n = len(C)

        def fn(k):
            # return true if it not exists a k-length subarray whose cost <=
            # budget
            q = deque()  # monotonic decreasing
            for i in range(n):
                # in
                while q and A[q[-1]] < A[i]:
                    q.pop()
                q.append(i)
                # out
                while q and i - q[0] >= k:
                    q.popleft()
                if i >= k - 1 and q and A[q[0]] + k * (C[i + 1] - C[i - k + 1]) <= b:
                    return False
            return True

        l, r = 0, len(A) + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return max(l - 1, 0)


# heap solution
class Solution:
    def maximumRobots(self, C: List[int], R: List[int], budget: int) -> int:
        C = [0] + C
        R = list(accumulate(R, initial=0))

        def fn(k):
            pqC = []
            for i in range(1, len(R)):
                while pqC and i - pqC[0][1] >= k:
                    heappop(pqC)
                heappush(pqC, (-C[i], i))
                if i >= k and pqC and -pqC[0][0] + k * (R[i] - R[i - k]) <= budget:
                    return True
            return False

        l, r = 0, len(C)
        while l < r:
            m = (l + r) // 2
            if not fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
