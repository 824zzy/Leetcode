# Greedy Heap

## When to Use

| Problem Signal | Technique |
|---|---|
| Maximize/minimize a score where one dimension is fixed at a time | Sort by one dimension, heap for the other (LC 1383, 857, 2542) |
| Select exactly k items where each impacts a global metric | Sort + sliding window with min/max heap (LC 1383, 857, 502) |
| Choose which tasks/items to keep when capacity is exceeded | Heap to track what to evict (LC 630, 1642) |
| Incrementally build a solution by always picking best available | Maintain heap of candidates, update after each choice (LC 1834, 2402) |
| Schedule tasks with deadlines or cooldowns | Sort by deadline, heap to track current state (LC 630, 1705, 358) |
| Distribute operations to minimize max or maximize min | Min heap for "fill gap" (LC 2233, 2333) |
| Reorganize elements to satisfy adjacency constraints | Max heap with frequency counts, greedily place highest (LC 358, 1405, 767) |

## Pattern 1: Sort One Dimension, Heap for the Other

The classic "pick k items to optimize a product" pattern. Sort by one attribute (usually the constraint or minimum), then use a heap to track the k best items for the other attribute as you iterate.

### Why it works

When you iterate in sorted order by dimension A, the current element becomes the new minimum for A in any solution that includes it. So you greedily select the k largest values for dimension B seen so far.

### Template

```py
# maximize: sum(k items from B) * min(k items from A)
# sort by A descending, so A[i] is the min of all items [0..i]
A = sorted(zip(B, A), key=lambda x: -x[1])
pq = []
sm = 0
ans = 0
for b, a in A[:k]:
    heappush(pq, b)
    sm += b
ans = sm * A[k - 1][1]

for b, a in A[k:]:
    heappush(pq, b)
    sm += b
    sm -= heappop(pq)  # evict smallest b
    ans = max(ans, sm * a)
return ans
```

**Variant: heapreplace for cleaner code**

```py
# initialize with first k
pq = [b for b, _ in A[:k]]
heapify(pq)
sm = sum(pq)
ans = sm * A[k - 1][1]

for b, a in A[k:]:
    sm += b + heapreplace(pq, b)  # heapreplace returns the evicted value
    ans = max(ans, sm * a)
```

### Examples

**LC 1383 - Maximum Performance of a Team**

Pick k engineers to maximize `sum(speed) * min(efficiency)`. Sort by efficiency descending, maintain min-heap of top k speeds.

```py
def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    A = sorted(zip(speed, efficiency), key=lambda x: -x[1])
    pq = []
    sm = ans = 0
    for s, e in A:
        heappush(pq, s)
        sm += s
        if len(pq) > k:
            sm -= heappop(pq)
        ans = max(ans, sm * e)
    return ans % (10 ** 9 + 7)
```

**LC 2542 - Maximum Subsequence Score**

Pick k items to maximize `sum(k from nums1) * min(k from nums2)`. Identical pattern.

**LC 857 - Minimum Cost to Hire K Workers**

Pick k workers to minimize `sum(wage) / sum(quality) * sum(quality)` = `sum(wage / quality) * sum(quality)`. The ratio acts as the efficiency dimension. Sort by ratio ascending, maintain max-heap (negated) of top k qualities.

```py
def mincostToHireWorkers(self, Q: List[int], W: List[int], k: int) -> float:
    A = sorted([(q, w / q) for q, w in zip(Q, W)], key=lambda x: x[1])
    pq = [-q for q, _ in A[:k]]
    heapify(pq)
    sm = -sum(pq)
    ans = sm * A[k - 1][1]
    for q, r in A[k:]:
        sm += q + heapreplace(pq, -q)
        ans = min(ans, sm * r)
    return ans
```

**LC 502 - IPO**

Pick k projects to maximize capital. Sort by capital required, use max-heap for profits.

```py
def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    A = sorted(zip(capital, profits))
    pq = []
    i = 0
    for _ in range(k):
        while i < len(A) and A[i][0] <= w:
            heappush(pq, -A[i][1])
            i += 1
        if pq:
            w -= heappop(pq)
    return w
```

## Pattern 2: Choose What to Evict

When you exceed capacity, use a heap to decide what to remove. Usually a max-heap (negated) to evict the largest item.

### Template

```py
pq = []
for x in stream:
    heappush(pq, -x)  # max-heap
    process(x)
    if exceed_capacity():
        evict(-heappop(pq))
```

### Examples

**LC 630 - Course Schedule III**

Take courses to maximize count, each has duration and deadline. Sort by deadline, if current time exceeds deadline, evict the longest course taken so far.

```py
def scheduleCourse(self, A: List[List[int]]) -> int:
    A.sort(key=lambda x: x[1])
    time = 0
    pq = []
    for duration, deadline in A:
        time += duration
        heappush(pq, -duration)
        while time > deadline:
            time += heappop(pq)  # heappop returns negative duration
    return len(pq)
```

**LC 1642 - Furthest Building You Can Reach**

Use bricks for climbs, but can replace the k largest climbs with ladders. Maintain max-heap of bricks used.

```py
def furthestBuilding(self, A: List[int], bricks: int, ladders: int) -> int:
    pq = []
    for i in range(len(A) - 1):
        diff = A[i + 1] - A[i]
        if diff <= 0:
            continue
        heappush(pq, -diff)
        bricks -= diff
        if bricks < 0:
            if ladders == 0:
                return i
            bricks += -heappop(pq)
            ladders -= 1
    return len(A) - 1
```

## Pattern 3: Fill Gap (Incremental Min-Heap)

Distribute k operations to minimize the maximum (or maximize the minimum). Pop the min, add 1, repeat. Optimization: if multiple elements have the same min value, batch the operations.

### Template

```py
heapify(A)
n = len(A)
while k:
    mn = heappop(A)
    gap = max(k // n, 1)  # batch size
    heappush(A, mn + gap)
    k -= gap
```

### Examples

**LC 2233 - Maximum Product After K Increments**

```py
def maximumProduct(self, A: List[int], k: int) -> int:
    heapify(A)
    n = len(A)
    while k:
        mn = heappop(A)
        gap = max(k // n, 1) if A else k
        heappush(A, mn + gap)
        k -= gap
    ans = 1
    for x in A:
        ans *= x
        ans %= 10 ** 9 + 7
    return ans
```

**LC 2333 - Minimum Sum of Squared Difference**

Distribute k operations to minimize sum of squares of differences. Use max-heap (negated) to always reduce the largest difference.

```py
def minSumSquareDiff(self, A: List[int], B: List[int], k1: int, k2: int) -> int:
    pq = [-abs(a - b) for a, b in zip(A, B)]
    if -sum(pq) <= k1 + k2:
        return 0
    heapify(pq)
    k = k1 + k2
    n = len(pq)
    while k:
        mx = heappop(pq)
        gap = max(k // n, 1) if pq else k
        heappush(pq, mx + gap)
        k -= gap
    return sum(x * x for x in pq)
```

## Pattern 4: Task Scheduling with Constraints

Heap to track availability or priority of tasks/resources.

### Template: Event-driven simulation

```py
events = sorted([(start, end, data) for ...])
pq = []  # available resources or pending tasks
for event in events:
    # process anything that became available/finished
    while pq and pq[0][0] <= event.time:
        heappop(pq)
    # handle current event
    heappush(pq, ...)
```

### Examples

**LC 1834 - Single-Threaded CPU**

Tasks have arrival time and duration. CPU picks available task with shortest duration (tie-break by index). Simulate time.

```py
def getOrder(self, tasks: List[List[int]]) -> List[int]:
    tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
    pq = []
    t = 0
    ans = []

    for i in range(len(tasks)):
        # process all available tasks before next arrival
        while pq and tasks[i][0] > t:
            duration, idx = heappop(pq)
            t += duration
            ans.append(idx)
        # advance time if CPU is idle
        t = max(t, tasks[i][0])
        heappush(pq, (tasks[i][1], tasks[i][2]))

    while pq:
        ans.append(heappop(pq)[1])
    return ans
```

**LC 2402 - Meeting Rooms III**

Assign meetings to rooms, track when each room becomes available.

```py
def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    meetings.sort()
    rooms = [(0, i, 0) for i in range(n)]  # (available_time, room_id, count)
    for start, end in meetings:
        # free rooms that are available
        for idx, (avail, room_id, cnt) in enumerate(rooms):
            if avail <= start:
                rooms[idx] = (0, room_id, cnt)
        heapify(rooms)
        avail, room_id, cnt = heappop(rooms)
        if avail <= start:
            heappush(rooms, (end, room_id, cnt + 1))
        else:
            heappush(rooms, (avail + (end - start), room_id, cnt + 1))
    return max(rooms, key=lambda x: (x[2], -x[1]))[1]
```

**LC 1705 - Maximum Number of Eaten Apples**

Apples rot after d days. Greedily eat the apple that will rot soonest (min-heap by expiration time).

```py
def eatenApples(self, A: List[int], D: List[int]) -> int:
    pq = []
    ans = 0
    for t, (a, d) in enumerate(zip(A, D)):
        # remove rotten apples
        while pq and pq[0][0] <= t:
            heappop(pq)
        # add new apples
        if a:
            heappush(pq, (t + d, a))
        # eat one apple
        if pq:
            pq[0][1] -= 1
            if pq[0][1] == 0:
                heappop(pq)
            ans += 1

    # continue eating after last day
    t += 1
    while pq:
        while pq and pq[0][0] <= t:
            heappop(pq)
        if not pq:
            break
        expire, count = heappop(pq)
        can_eat = min(count, expire - t)
        t += can_eat
        ans += can_eat
    return ans
```

## Pattern 5: Reorganize String with Constraints

Rebuild a string/sequence to satisfy adjacency constraints. Use max-heap of frequencies, greedily place the most frequent valid character.

### Template

```py
cnt = Counter(s)
pq = [(-freq, char) for char, freq in cnt.items()]
heapify(pq)
ans = []
while pq:
    freq, char = heappop(pq)
    if can_place(ans, char):
        ans.append(char)
        if freq + 1 < 0:
            heappush(pq, (freq + 1, char))
    else:
        if not pq:
            return ""  # impossible
        freq2, char2 = heappop(pq)
        ans.append(char2)
        if freq2 + 1 < 0:
            heappush(pq, (freq2 + 1, char2))
        heappush(pq, (freq, char))
```

### Examples

**LC 767 - Reorganize String**

No two adjacent characters can be the same. Greedily place the most frequent character, unless it was just used.

```py
def reorganizeString(self, s: str) -> str:
    cnt = Counter(s)
    pq = [(-freq, char) for char, freq in cnt.items()]
    heapify(pq)
    ans = []
    while pq:
        freq, char = heappop(pq)
        if ans and ans[-1] == char:
            if not pq:
                return ""
            freq2, char2 = heappop(pq)
            ans.append(char2)
            if freq2 + 1 < 0:
                heappush(pq, (freq2 + 1, char2))
            heappush(pq, (freq, char))
        else:
            ans.append(char)
            if freq + 1 < 0:
                heappush(pq, (freq + 1, char))
    return "".join(ans)
```

**LC 1405 - Longest Happy String**

Same as 767 but constraint is no 3 consecutive.

```py
def longestDiverseString(self, a: int, b: int, c: int) -> str:
    pq = [(-x, ch) for x, ch in zip([a, b, c], "abc") if x]
    heapify(pq)
    ans = []
    while pq:
        freq, char = heappop(pq)
        if ans[-2:] == [char, char]:
            if not pq:
                break
            freq2, char2 = heappop(pq)
            ans.append(char2)
            if freq2 + 1 < 0:
                heappush(pq, (freq2 + 1, char2))
            heappush(pq, (freq, char))
        else:
            ans.append(char)
            if freq + 1 < 0:
                heappush(pq, (freq + 1, char))
    return "".join(ans)
```

**LC 358 - Rearrange String k Distance Apart**

Characters must be at least k positions apart. Use a busy queue to track when each character becomes available again.

```py
def rearrangeString(self, s: str, k: int) -> str:
    cnt = Counter(s)
    free = [(-freq, char) for char, freq in cnt.items()]
    heapify(free)
    busy = []  # (index_available, freq, char)
    ans = []

    while len(ans) != len(s):
        # move characters from busy to free
        if busy and len(ans) - busy[0][0] >= k:
            _, freq, char = busy.pop(0)
            heappush(free, (freq, char))

        if not free:
            return ""

        freq, char = heappop(free)
        ans.append(char)
        if freq + 1 < 0:
            busy.append((len(ans), freq + 1, char))

    return "".join(ans)
```

**LC 2182 - Construct String With Repeat Limit**

Build lexicographically largest string where no character repeats more than repeatLimit times consecutively. Use max-heap of characters, place as many copies as allowed, then switch to next character.

## Key Insights

1. **Sort to fix one dimension**: when the problem involves two dimensions (value + constraint, or two competing metrics), sort by one to make it monotonic, then use heap for the other.

2. **Heap for "current best"**: if you're building a solution incrementally and need to know the k best (or worst) items seen so far, maintain a size-k heap.

3. **Heap for eviction**: when capacity is exceeded, heap tells you what to remove. Max-heap to evict largest, min-heap to evict smallest.

4. **Simulation needs event ordering**: for time-based problems, sort events by time, use heap to track pending/available items.

5. **Frequency problems = max-heap**: when reorganizing elements with frequency constraints, always place the most frequent valid element next.

6. **Fill gap = amortized O(log n)**: repeatedly popping min and incrementing seems like O(k log n), but if you batch operations when many elements have the same min value, it becomes much faster in practice.

## Python heapq Cheat Sheet

```py
from heapq import heappush, heappop, heapify, heapreplace

# min-heap by default
pq = []
heappush(pq, 5)
heappush(pq, 3)
heappop(pq)  # returns 3

# max-heap: negate values
pq = []
heappush(pq, -5)
heappush(pq, -3)
-heappop(pq)  # returns 5

# heapify in-place: O(n)
A = [5, 3, 7, 1]
heapify(A)  # A is now a valid heap

# heapreplace: pop then push in one operation
# more efficient than heappop + heappush
old = heapreplace(pq, 10)  # returns min, pushes 10

# heappushpop: push then pop in one operation
# even more efficient if you know you'll immediately pop
val = heappushpop(pq, 10)  # pushes 10, returns min

# nsmallest / nlargest: get k smallest/largest without removing
from heapq import nsmallest, nlargest
nsmallest(3, A)  # [1, 3, 5]
nlargest(2, A)   # [7, 5]

# custom key: use tuples
# heap compares tuples lexicographically
heappush(pq, (priority, value))
heappush(pq, (priority, tie_breaker, value))
```
