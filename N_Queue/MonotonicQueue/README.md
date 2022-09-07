# Monotonic Queue

Monotonic queue is also known as dequeue since the monotonicity is ensured by continuously popping element from left and right.
This technique is used to solve "Sliding Window Maximum/Minimum" problem (base template is Problem 239).

More specifically, the hardest part of monotonic queue is to find out what is the condition to pop left and right.

In general, the rule of thumb of the conditions in Chinese is "年老色衰", "年老" refer to the left-most element is **too "old" to stay in deque**;
"色衰" refer to the right-most element is **too "ugly" compare to the up-coming element**.

## Template

``` py
# Heap implementation
pq = []
for i in range(len(A)):
    while pq and CONDITION:
        UPDATE_ANS
        heappop(pq)
    heappush(pq, ITEM) # ITEM usually is (A[i], i)
```

``` py
# Dequeue implementation
dq = deque()
for i, x in enumerate(A):
    # pop left element if its index out of window size
    while dq and CONDITION2: dq.popleft()
    # monotonic decreasing queue
    while dq and CONDITION1: dq.pop()
    dq.append((i, x))
```

The monotonic priority queue problems are essentially a type of greedy and sliding window problem.
The problem usually gives you a threshold, and you have to leverage the threshold to find out the condition to update priority queue.

TODO: https://leetcode.com/tag/monotonic-queue/