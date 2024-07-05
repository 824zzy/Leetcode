""" https://leetcode.com/problems/task-scheduler/
let min(n, len(pq)) be the stride, and simulate the process by priority queue.
"""
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        n += 1
        cnt = Counter(tasks)
        ans = 0
        pq = [-v for k, v in cnt.items()]
        heapify(pq)

        while pq:
            tmp = []
            k = min(n, len(pq))
            for _ in range(n):
                if pq:
                    v = -heappop(pq)
                    if v - 1 > 0:
                        tmp.append(-(v - 1))
            if tmp:
                ans += n
            else:
                ans += k
            pq.extend(tmp)
        return ans


""" A tricky math solution
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        most_occurence = max([value for value in counter.values()])
        num_keys = len([key for key in counter if counter[key] == most_occurence])

        gapCount = most_occurence - 1
        gapLength = n - (num_keys - 1)
        empty_slots = gapCount * gapLength
        available_tasks = len(tasks) - num_keys * most_occurence

        idles = max(0, empty_slots - available_tasks)

        return idles + len(tasks)
