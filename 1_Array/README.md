# Note

## Operations

1. `If Else` in `For`: `[a if cond1 else cond2 for a in A]`
2. Jump steps in a list: `list[::step]`

## Modules

### Counter

1. `Counter.most_common(num)`: return a list contains tuple.
2. `del Counter[key]`: delete an item. or `Counter[key]=0`

### OrderedDict

### Heap

1. `heapq.heappush(heap, item)`: Push the value item onto the heap, maintaining the heap invariant.
2. `heapq.heappop(heap)`: Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
3. `heapq.heapify(x)`: Transform list x into a heap, in-place, **in linear time**.
4. `heapq.nlargest/nsmallest(n, iterable[, key])`: Return a list with the n largest elements from the dataset defined by iterable.
