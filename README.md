# Leetcode fun

One question a day to ensure a sharp mind.

## Grading Criteria

- `L0`: straight forward question
- `L1`: variance of template
- `L2`: need to think for a while / complex implementation
- `L3`: need aha moment / unexpected algorithm

## Time Complexity Analysis

Row: input size(IS), column: time complexity(TC)

| IS&TC       |O($2^n$) |O($n^4$) |O($n^3$) |O($n^2$) |O(nlogn) | O(n)    | O(logn) |  O(1)   |
|  ---        | ---     |  ---    |  ---    |  ---    |  ---    |  ---    |  ---    |  ---    |
| 1-10        | &check; | &check; | &check; | &check; | &check; | &check; | &check; | &check; |
| 10-50       | &check; | &check; | &check; | &check; | &check; | &check; | &check; | &check; |
| 50-100      | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; | &check; |
| 100-500     | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; | &check; |
| 500 - $10^3$  | &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; |
|$10^3$ - $10^4$| &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; |
|$10^4$ - $10^5$| &cross; | &cross; | &cross; | &quest; | &check; | &check; | &check; | &check; |
|$10^5$ - $10^6$| &cross; | &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; |
|$10^6$ - $10^9$| &cross; | &cross; | &cross; | &cross; | &cross; | &cross; | &check; | &check; |

| TC       |  Algorithm                                                           |
|---       |   ---                                                                |
| O($2^n$) | DFS-combination($2^n$), DFS-permutation(n!),                                     |
| O($n^4$) | DP                                                                   |
| O($n^3$) | DP, Floyd-Warshall                                                   |
| O($n^2$) | DP                                                                   |
| O(nlogn) | Sorting, Heap, divide&conquer, Dijkstra-heap, QuickSort              |
| O(n)     | DP, DFS-tree(V), BFS(V+E), TopologicalSorting(V+E), BucketSort(N+K), MonotonicStack()  |
| O(logn)  | BinarySearch,  BinaryIndexTree|
| O(1)     | Math                                                                 |

## Trigger keywords

1. What is the data size?
2. Can I use DP?
3. Can I sort the array to use greedy or binary search?
4. Can I use two passes?
5. Can I solve it reversely?
6. Can I convert the problem to a other problem?

## Python Basic

### Operations

1. `[a if cond1 else cond2 for a in A]`: `if-else` statement in `for` loop
2. `A[::i]`: jump i-steps in a list, e.g., odd index elements `A[::2]` and even index elements `A[1::2]`
3. `A.insert(0, n)`: insert item to list by a specific index
4. `arr.sort(key=lambda x: (cond1, cond2, ..))`: sort array by multiple conditions. Condition can be `len(x)`, `x` #720
5. `sorted(list, key=functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))`: custom compare function to a list

### String

1. `str.startswith(s)`: returns True if the string starts with the specified value, otherwise False

### Set

1. `s.add(x)`: add value x to set s. Time: O(1)
2. `s1.update(s2)`: add set s2 to set s1. Time: O(len(s2))

### Hash Table

1. `Counter.most_common(num)`: return a list contains tuple.
2. `del Counter[key]`: delete an item. or `Counter[key]=0`.
3. `cntA+cntB`: add two counters together.
4. `cntA-cntB`: subtract (keeping only positive counts).
5. `cntA&cntB`: find intersection of two counters. min(cntA, cntB)
6. `cntA|cntB`: find union of two counters. max(cntA, cntB)

### Heap

1. `heapq.heappush(heap, item)`: Push the value item onto the heap, maintaining the heap invariant.
2. `heapq.heappop(heap)`: Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
3. `heapq.heapify(x)`: Transform list x into a heap, in-place, **in linear time**.
4. `heapq.nlargest/nsmallest(n, iterable[, key])`: Return a list with the n largest elements from the dataset defined by iterable.

## Reference

1. [用什么语言刷题？C++/Java/Python横向大比较](https://www.youtube.com/watch?v=ZyCQBrcr6jk&list=PLLuMmzMTgVK7XfFadhkPuF_ztvhxbriDr&index=7)
2. [Leetcode 101: A Leetcode Grinding Guide(C++ Version)](https://github.com/changgyhub/leetcode_101)
3. [Algorithms for Competitive Programming](https://cp-algorithms.com/)
4. [古城算法 slides(google drive)](https://drive.google.com/drive/folders/17I-0mEeaY8X5j7RRMh0x_a2zNLu7jafq)
5. [输入数据规模和时间复杂度的关系](https://www.youtube.com/watch?v=eG99FDBeuJo)
