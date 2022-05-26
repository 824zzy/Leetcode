# Monotonic Priority Queue

The monotonic priority queue problems are essentially a type of greedy with the help of priority queue.
The problem usually gives you a threshold, and you have to leverage the threshold to update priority queue and find the final answer.

## Template

``` py
def monotonic_priority_queue(self, A):
    t = 0  # set threshold to pop heap
    pq = []
    ans
    for i in range(len(A)):
        while pq and THRESHOLD:
            UPDATE_ANS
            heappop(pq)
        heappush(pq, ITEM)
    return ans
```

TODO: https://leetcode.com/tag/monotonic-queue/
