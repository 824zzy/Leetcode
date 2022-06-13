# Monotonic Queue

Monotonic queue is also known as dequeue since the monotonicity is ensured by continuously poping element from left and right.
More specifically, the hardest part of monotonic queue is to find out what is the condition to pop left and right.
In general, the rule of thumb of the conditions in Chinese is "年老色衰", "年老" refer to the left-most element is **too "old" to stay in deque**;
"色衰" refer to the right-most element is **too "ugly" compare to the up-coming element**.

``` py
dq = deque()
for i, x in enumerate(A):
    # monotonic decreasing queue
    while dq and CONDITION1: dq.pop()
    # pop left element if its index out of window size
    while dq and CONDITION2: dq.popleft()
    dq.append((i, x))
```
