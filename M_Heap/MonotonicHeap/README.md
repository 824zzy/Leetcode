# Monotonic Priority Queue

The monotonic priority queue problems are essentially a type of greedy with the help of priority queue.
The problem usually gives you a threshold, and you have to leverage the threshold to find out the condition to update priority queue.

## Template

``` py
pq = []
for i in range(len(A)):
    while pq and CONDITION:
        UPDATE_ANS
        heappop(pq)
    heappush(pq, ITEM) # ITEM usually is (A[i], i)
```

TODO: https://leetcode.com/tag/monotonic-queue/
