# Monotonic Priority Queue

## Template

TODO: update template

``` py
def monotonic_priority_queue(self, A: List[List[int]]) -> int:
    A = sorted(A, key=lambda x: x[1])
    t = 0  # set threshold to pop heap
    pq = []
    for x, y in A:
        t += x # update threshold value
        heappush(pq, -x)
        while t>y: t += heappop(pq)
    return ?
```

TODO: https://leetcode.com/tag/monotonic-queue/
