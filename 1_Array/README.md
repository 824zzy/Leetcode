# Note

## Operations

1. `If Else` in `For`: `[a if cond1 else cond2 for a in A]`
2. Jump steps in a list: `list[::step]`
3. Insert item to list with specific index: `stk.insert(0, n)`
4. Sort array by multiple conditions: `arr.sort(key=lambda x: (cond1, cond2, ..))`. Condition can be `len(x)`, `x` #720
5. `sorted(list, key=functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))`: custom compare function to a list

## Modules

### Counter

1. `Counter.most_common(num)`: return a list contains tuple.
2. `del Counter[key]`: delete an item. or `Counter[key]=0`.
3. `cntA+cntB`: add two counters together.
4. `cntA-cntB`: subtract (keeping only positive counts).
5. `cntA&cntB`: find intersection of two counters. min(cntA, cntB)
6. `cntA|cntB`: find union of two counters. max(cntA, cntB)

### OrderedDict

### Heap

1. `heapq.heappush(heap, item)`: Push the value item onto the heap, maintaining the heap invariant.
2. `heapq.heappop(heap)`: Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
3. `heapq.heapify(x)`: Transform list x into a heap, in-place, **in linear time**.
4. `heapq.nlargest/nsmallest(n, iterable[, key])`: Return a list with the n largest elements from the dataset defined by iterable.
