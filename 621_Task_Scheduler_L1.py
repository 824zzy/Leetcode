from collections import Counter
class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        queue = []
        while counter:
            temp = []
            task = counter.most_common()
            if task in queue:
                
                queue.append(task)
                counter[task]
        
s = Solution()
s.leastInterval(["A","A","A","B","B","B"], 2)