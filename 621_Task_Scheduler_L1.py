""" Simulation by heap
"""
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counter = Counter(tasks)
        count = 0
        cycle = n + 1
        heap = []
        
        for k, i in counter.items():
                heapq.heappush(heap, -i)
        
        while heap:
            works = [heapq.heappop(heap) for i in range(cycle) if heap]
            worktime = len(work)
            for work in works:
                work = work * (-1) - 1
                if work > 0:
                    heapq.heappush(heap, -work)
            count += cycle if len(heap) > 0 else worktime
        
        return count

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