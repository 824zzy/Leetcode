# Heap

## Basic operations

1. `heapq.heappush(heap, item)`: Push the value item onto the heap, maintaining the heap invariant. Time complexity: O(log n)
2. `heapq.heappop(heap)`: Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0]. Time complexity: O(log n)
3. `heapq.heapify(x)`: Transform list x into a heap, in-place, **in linear time O(n)**.
4. `heapq.nlargest/nsmallest(n, iterable[, key])`: Return a list with the n largest elements from the dataset defined by iterable.
