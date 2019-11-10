""" Simulation by heap
"""
from collections import Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        counter, ans, cycle = Counter(tasks), 0, n+1
        heap = []
        for k, v in counter.items():
            # maintain a maxHeap
            heappush(heap, -v)
        while heap:
            works = [heappop(heap) for i in range(cycle) if heap]
            worktime = len(works)
            for work in works:
                work = work*(-1) - 1
                if work>0:
                    heappush(heap, -work)
            ans += cycle if len(heap)>0 else worktime
        return ans

""" A tricky math solution
"""
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        
        most_occurence = max([value for value in counter.values()])
        num_keys = len([key for key in counter if counter[key]==most_occurence])
        
        gapCount = most_occurence - 1
        gapLength = n - (num_keys - 1)
        empty_slots = gapCount * gapLength
        available_tasks = len(tasks) - num_keys * most_occurence
        
        idles = max(0, empty_slots-available_tasks)
        
        return idles+len(tasks)