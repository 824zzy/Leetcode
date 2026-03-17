# Leetcode for fun

One question a day to ensure a sharp mind.

## Grading Criteria

- `L0`: straight forward question
- `L1`: variance of template
- `L2`: need to think for a while / complex implementation
- `L3`: need aha moment / unexpected algorithm

## Roadmap

Study-order progression through all topic areas. Each entry links to the topic README with templates and notes.

### Fundamentals

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 1 | String | [README](A_Basic/String/README.md) | String operations, Counter API |
| 2 | Hash Table | [README](B_HashTable/README.md) | Counter operations, mapping |
| 3 | Linked List | [README](C_LinkList/README.md) | Reverse, fast/slow pointers |
| 4 | Two Pointers | [README](D_TwoPointers/README.md) | Same/different direction templates |
| 5 | Sliding Window | [README](E_SlidingWindow/README.md) | Fixed/dynamic window, at-most trick |
| 6 | Prefix Sum | [README](F_PrefixSum/README.md) | 1D/2D prefix sum, difference array |
| 7 | Binary Search | [README](G_BinarySearch/README.md) | Template, bisect module |
| 8 | Stack | [README](L_Stack/README.md) | Monotonic stack, Eulerian path, tree traversal |
| 9 | Monotonic Queue | [README](N_Queue/MonotonicQueue/README.md) | Sliding window max/min by deque |
| 10 | Histogram | [README](A_Basic/Matrix/Histogram/README.md) | Histogram model for matrices |

### Search and Graph

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 11 | BFS | [README](I_Searching/BFS/README.md) | Graph BFS template |
| 12 | BFS Tree | [README](I_Searching/BFS/Tree/README.md) | Tree level-order traversal |
| 13 | BFS/DFS Graph | [README](I_Searching/BFS/Graph/README.md) | Matrix and graph DFS |
| 14 | Dijkstra | [README](I_Searching/BFS/Dijkstra/README.md) | Single-source shortest path |
| 15 | Floyd-Warshall | [README](I_Searching/BFS/Floyd-Warshall/README.md) | All-pairs shortest path |
| 16 | DFS Tree | [README](I_Searching/DFS/Tree/README.md) | Tree DFS traversal templates |
| 17 | LCA | [README](I_Searching/DFS/LowestCommonAncestor/README.md) | Lowest common ancestor, binary lifting |
| 18 | Backtracking | [README](H_Backtracking/README.md) | Pruning, array/graph templates |

### Dynamic Programming

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 19 | DP Overview | [README](K_DynamicProgramming/README.md) | Categories, matrix exponentiation |
| 20 | Knapsack | [README](K_DynamicProgramming/Knapsack/README.md) | 0/1 and unbounded knapsack |
| 21 | LIS | [README](K_DynamicProgramming/LongestIncreasingSubsequence/README.md) | O(n^2) and O(n log n) |
| 22 | Longest Subsequence | [README](K_DynamicProgramming/LongestSubsequence/README.md) | LIS/LCS templates |
| 23 | Kadane | [README](K_DynamicProgramming/Kadane(MaximumSubarray)/README.md) | Maximum subarray |
| 24 | Digit DP | [README](K_DynamicProgramming/DigitDP/README.md) | Digit DP templates with bounds |

### Greedy and Math

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 25 | Greedy | [README](Q_Greedy/README.md) | Assign/interval problems |
| 26 | Math | [README](S_Math/README.md) | GCD/LCM, sieve, math functions |
| 27 | Combinatorics | [README](S_Math/Combinatorics/README.md) | Product rule, C(n,k), permutations |
| 28 | Primes | [README](S_Math/NumberTheory/Prime/README.md) | Sieve, factorization, LPF |
| 29 | Bezout's Lemma | [README](S_Math/NumberTheory/Bezout'sLemma/README.md) | Extended GCD |
| 30 | Game Theory | [README](S_Math/GameTheory/README.md) | Minimax |
| 31 | Probability | [README](S_Math/Probability/README.md) | Reservoir sampling, shuffle |
| 32 | Bit Manipulation | [README](R_BitManipulation/README.md) | Bit operations, bitmask DP |

### Advanced Data Structures

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 33 | Trie | [README](O_Trie/Trie/README.md) | Insert, search, prefix |
| 34 | Union-Find | [README](P_UnionFind/README.md) | Path compression, union by rank, Kruskal's |
| 35 | Binary Indexed Tree | [README](Z_Advanced/BinaryIndexedTree/README.md) | Fenwick tree |
| 36 | Segment Tree | [README](Z_Advanced/SegmentTree/README.md) | Tree/array/ZKW, lazy propagation |
| 37 | Sorted Containers | [README](Z_Advanced/SortedContainers/README.md) | SortedList complexity reference |

### Advanced Algorithms

| # | Topic | README | Description |
|---|-------|--------|-------------|
| 38 | Sorting | [README](Z_Advanced/Sorting/README.md) | Cycle sort |
| 39 | KMP | [README](Z_Advanced/PatternSearching/KMP/README.md) | KMP pattern matching |
| 40 | Z-Function | [README](Z_Advanced/PatternSearching/Z-Function/README.md) | Z-function pattern matching |
| 41 | Prim | [README](N_Queue/Prim/README.md) | Minimum spanning tree |
| 42 | Majority Voting | [README](_misc/Majority_Voting/README.md) | Boyer-Moore voting |
| 43 | Rolling Hash | [README](_misc/Hash/RollingHash/README.md) | Rabin-Karp |
| 44 | Greedy Heap | [README](N_Queue/GreedyHeap/README.md) | Heap-based greedy patterns |
| 45 | SQL | [README](_misc/SQL/README.md) | Query categories |
| 46 | System Design | [README](_misc/System_Design/README.md) | General steps |

## Running Solutions

Solutions depend on `header.py` for shared imports and class definitions. Use the runner script:

```sh
python run.py path/to/solution.py
```

This pre-loads `header.py` into the namespace before executing the solution file.

## Time Complexity Analysis

Row: input size(IS), column: time complexity(TC)

| Input Size | O($2^n$) | O($n^4$) | O($n^3$) | O($n^2$) | O(nlogn) | O(n) | O(logn) | O(1) |
|---|---|---|---|---|---|---|---|---|
| 1-10 | &check; | &check; | &check; | &check; | &check; | &check; | &check; | &check; |
| 10-50 | &check; | &check; | &check; | &check; | &check; | &check; | &check; | &check; |
| 50-100 | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; | &check; |
| 100-500 | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; | &check; |
| 500 - $10^3$ | &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; |
| $10^3$ - $10^4$ | &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; | &check; |
| $10^4$ - $10^5$ | &cross; | &cross; | &cross; | &quest; | &check; | &check; | &check; | &check; |
| $10^5$ - $10^6$ | &cross; | &cross; | &cross; | &cross; | &check; | &check; | &check; | &check; |
| $10^6$ - $10^9$ | &cross; | &cross; | &cross; | &cross; | &cross; | &cross; | &check; | &check; |

| TC       | Algorithm |
|----------|-----------|
| O($2^n$) | DFS-combination($2^n$), DFS-permutation(n!) |
| O($n^4$) | DP |
| O($n^3$) | DP, Floyd-Warshall |
| O($n^2$) | DP |
| O(nlogn) | Sorting, Heap, divide&conquer, Dijkstra-heap, QuickSort |
| O(n)     | DP, DFS-tree(V), BFS(V+E), TopologicalSorting(V+E), BucketSort(N+K), MonotonicStack |
| O(logn)  | BinarySearch, BinaryIndexTree |
| O(1)     | Math |

## Approach Checklist

1. What is the data size? (check the [time complexity table](#time-complexity-analysis))
2. Can I sort or group the elements?
3. Can I use DP, greedy, or binary search?
4. Can I enumerate on a specific variable? (fix one dimension, solve the other)
5. Can I use two passes? (left-to-right, then right-to-left)
6. Can I solve it in reverse order?
7. Can I convert it to a known problem?
8. Is there monotonicity I can exploit? (binary search on answer)
9. Can I decompose into prefix and suffix? (prefix-suffix decomposition)
10. Does the answer have optimal substructure (DP) or the greedy-choice property (greedy)?
11. See the [Pattern Recognition Guide](#pattern-recognition-guide) for keyword-based technique selection.

## Pattern Recognition Guide

When you spot these keywords or structural patterns in a problem, consider the listed techniques first.

### Array and Subarray

| Signal / Keyword | Techniques to Consider |
|---|---|
| "subarray" (general) | sliding window, monotonic stack/queue, prefix sum + hash table, Kadane's |
| "subarray sum equals k" | prefix sum + hash table |
| "at most k" / "at least k" / "exactly k" | at-most trick: f(k) - f(k-1) |
| "longest/shortest subarray with condition" | sliding window (dynamic window) |
| "max/min subarray sum" | Kadane's, prefix sum |
| "number of subarrays where..." | sliding window counting, prefix sum + hash table |
| "contiguous elements" | sliding window, prefix sum |
| "difference between elements in window" | sliding window + hash/sorted structure |
| "range update on array" | difference array (sweep line) |
| "range query (static)" | prefix sum, 2D prefix sum |
| "range query (dynamic / with updates)" | segment tree, BIT (Fenwick tree) |
| "next greater/smaller element" | monotonic stack |
| "sliding window max/min" | monotonic deque |

### Subsequence

| Signal / Keyword | Techniques to Consider |
|---|---|
| "subsequence" (general) | DP (LIS/LCS), two pointers, greedy |
| "longest increasing subsequence" | O(n log n) patience sort with bisect |
| "longest common subsequence" | 2D DP |
| "count subsequences" | DP, combinatorics |
| "subsequence with constraint" | DP with extra state |
| "two sequences / edit distance" | double-sequence DP |

### Optimization and Search

| Signal / Keyword | Techniques to Consider |
|---|---|
| "minimize the maximum" / "maximize the minimum" | binary search on answer |
| "kth smallest/largest" | binary search, heap, quick select |
| "minimum cost / operations to..." | DP, BFS (shortest path), greedy |
| "is it possible to..." | DP, greedy, graph reachability, math |
| "count number of ways" | DP, combinatorics |
| "find all / generate all" | backtracking, BFS/DFS |
| "optimal strategy for two players" | minimax, game theory DP |
| "buy and sell / state transitions" | state machine DP or greedy |

### String

| Signal / Keyword | Techniques to Consider |
|---|---|
| "palindrome" | two pointers (expand from center), Manacher's, DP |
| "anagram" | Counter / sorting, sliding window |
| "substring matching" | sliding window, rolling hash (Rabin-Karp), KMP, Z-function |
| "pattern matching" | KMP, Z-function, rolling hash |
| "parentheses / brackets" | stack, greedy |
| "string transformation / edit distance" | DP (double-sequence) |
| "repeated pattern in string" | KMP failure function, Z-function |
| "decode / parse string" | stack, recursion, DP |

### Graph

| Signal / Keyword | Techniques to Consider |
|---|---|
| "connected components" | Union-Find, BFS/DFS |
| "shortest path (unweighted)" | BFS |
| "shortest path (weighted, non-negative)" | Dijkstra |
| "shortest path (all pairs)" | Floyd-Warshall |
| "shortest path (negative edges)" | Bellman-Ford |
| "cycle detection (directed)" | DFS 3-coloring (white/gray/black) |
| "cycle detection (undirected)" | Union-Find, DFS with parent tracking |
| "topological order / prerequisites / dependency" | topological sort (Kahn's BFS) |
| "bipartite / 2-colorable" | BFS/DFS 2-coloring |
| "MST / minimum cost to connect all" | Kruskal's (Union-Find), Prim's (heap) |
| "number of islands / flood fill" | BFS/DFS, Union-Find |
| "word ladder / transformation sequence" | BFS |

### Tree

| Signal / Keyword | Techniques to Consider |
|---|---|
| "lowest common ancestor (LCA)" | binary lifting, recursive DFS |
| "tree diameter / longest path" | two BFS, or DFS returning depth |
| "rerooting / answer for every node as root" | tree DP with moving root |
| "subtree queries" | DFS + Euler tour (in/out time), post-order |
| "path sum / path queries" | LCA + prefix sums on tree, DFS |
| "binary tree traversal" | recursive DFS, iterative with stack |
| "serialize / deserialize tree" | pre-order + null markers, level-order |

### Matrix / Grid

| Signal / Keyword | Techniques to Consider |
|---|---|
| "2D grid traversal / islands / regions" | BFS/DFS |
| "largest rectangle in matrix" | histogram model + monotonic stack |
| "2D range sum / submatrix sum" | 2D prefix sum |
| "shortest path in grid" | BFS (unweighted), Dijkstra (weighted cells) |
| "rotate / spiral / layer traversal" | simulation with boundary tracking |

### Interval

| Signal / Keyword | Techniques to Consider |
|---|---|
| "merge intervals" | sort by start |
| "non-overlapping / max intervals" | sort by end, greedy |
| "interval scheduling / meeting rooms" | sort by end (greedy), sweep line |
| "overlapping interval count / max overlap" | sweep line, difference array |
| "insert interval" | binary search or linear merge |
| "range add/set then query" | difference array, segment tree + lazy propagation |

### Counting and Combinatorics

| Signal / Keyword | Techniques to Consider |
|---|---|
| "permutation" | backtracking, n!, next_permutation |
| "combination / choose k from n" | C(n,k), Pascal's triangle, backtracking |
| "number of ways to partition/arrange" | DP, combinatorics (product rule) |
| "divisibility / GCD / LCM" | number theory, Euclidean algorithm |
| "prime / factorization" | sieve of Eratosthenes, LPF (least prime factor) |
| "modulo arithmetic / large results mod 10^9+7" | modular exponentiation, Fermat's little theorem |

### Data Structure Selection

| Signal / Keyword | Techniques to Consider |
|---|---|
| "dynamic sorted data / rank queries" | SortedList, segment tree, BIT |
| "prefix/suffix lookups with updates" | BIT (Fenwick tree), segment tree |
| "string prefix queries / autocomplete" | trie |
| "disjoint sets / union / merge groups" | Union-Find (DSU) |
| "median maintenance / top-k from stream" | two heaps (max-heap + min-heap), SortedList |
| "frequent element / majority element" | Boyer-Moore voting |
| "merge k sorted lists/arrays" | heap (priority queue) |
| "LRU / LFU / ordered access" | hash map + doubly linked list, OrderedDict |
| "rearrange to avoid adjacent duplicates" | greedy with max-heap |

---

### Advanced / Niche Patterns

Less frequent, but important to recognize when they show up.

#### State Compression and Bitmask

| Signal / Keyword | Techniques to Consider |
|---|---|
| "visit all nodes/cities (TSP)" | bitmask DP, n ≤ 20 |
| "subset enumeration / powerset" | bitmask iteration, backtracking |
| n ≤ 20 with combinatorial constraint | bitmask DP |
| "assign items to groups with constraints" | bitmask DP, backtracking |
| "XOR of subsets" | bitmask enumeration, linear algebra over GF(2) |

#### Digit DP

| Signal / Keyword | Techniques to Consider |
|---|---|
| "count numbers in [L, R] with digit property" | digit DP (tight/free bound) |
| "numbers with digit sum / digit constraint" | digit DP with state for constraint |
| "no repeated digits / specific digit pattern" | digit DP with bitmask or set tracking |

#### Interval DP

| Signal / Keyword | Techniques to Consider |
|---|---|
| "merge stones / matrix chain multiplication" | interval DP, O(n³) |
| "minimum cost to merge / burst balloons" | interval DP |
| "palindrome partitioning (min cuts)" | interval DP or DP with greedy |
| "optimal game (pick from ends)" | interval DP (minimax on range) |

#### Advanced DP Variants

| Signal / Keyword | Techniques to Consider |
|---|---|
| "recurrence with very large n (10^9+)" | matrix exponentiation |
| "expected value / probability of state" | probability DP |
| "tree + optimal substructure" | tree DP (post-order aggregation) |
| "DP transitions too slow" | data structure optimized DP (monotonic queue, segment tree, convex hull trick) |
| "DP depends on future decisions" | solve in reverse, or reformulate state |
| "DP on permutation / arrangement" | permutation DP, profile DP |

#### Advanced Graph

| Signal / Keyword | Techniques to Consider |
|---|---|
| "Euler path / circuit / use every edge once" | Hierholzer's algorithm |
| "strongly connected components" | Tarjan's, Kosaraju's |
| "bridges / articulation points" | Tarjan's DFS |
| "network flow / max matching" | max-flow (Dinic's), Hungarian algorithm |
| "negative cycle detection" | Bellman-Ford |

#### Advanced String

| Signal / Keyword | Techniques to Consider |
|---|---|
| "longest palindromic substring" | Manacher's O(n), expand around center |
| "string hashing / duplicate substring detection" | rolling hash (Rabin-Karp) |
| "suffix queries / longest repeated substring" | suffix array |
| "XOR queries on binary representations" | bitwise trie |

#### Specialized Sorting

| Signal / Keyword | Techniques to Consider |
|---|---|
| "place each element at its correct index" | cycle sort |
| "sort with limited value range" | counting sort, bucket sort |
| "find kth element without full sort" | quick select, O(n) average |
| "count inversions / merge-based counting" | merge sort |

#### Math Niche

| Signal / Keyword | Techniques to Consider |
|---|---|
| "express n as sum of squares" | Lagrange's four-square theorem |
| "linear combination of a and b" | Bezout's lemma, extended GCD |
| "random sampling from stream" | reservoir sampling |
| "random sampling from region" | rejection sampling |
| "fair shuffle" | Fisher-Yates shuffle |
| "game with optimal play (Nim, Sprague-Grundy)" | Sprague-Grundy theorem, XOR of pile sizes |
| "cellular automaton / Game of Life" | simulation with state encoding |
| "circular array" | modulo indexing, or duplicate the array |

## Cheat sheet

### Palindrome
Efficiently find all the palindrome numbers in a range 10**9:

```py
pal = []
base = 1
while base <= 10000:
    # odd number
    for i in range(base, base * 10):
        x = i
        t = i // 10
        while t:
            x = x * 10 + t % 10
            t //= 10
        pal.append(x)
    # even number
    if base <= 1000:
        for i in range(base, base * 10):
            x = t = i
            while t:
                x = x * 10 + t % 10
                t //= 10
            pal.append(x)
    base *= 10
pal.append(1_000_000_001)  # sentinel
```

## Reference

1. [用什么语言刷题？C++/Java/Python横向大比较](https://www.youtube.com/watch?v=ZyCQBrcr6jk&list=PLLuMmzMTgVK7XfFadhkPuF_ztvhxbriDr&index=7)
2. [Leetcode 101: A Leetcode Grinding Guide(C++ Version)](https://github.com/changgyhub/leetcode_101)
3. [Algorithms for Competitive Programming](https://cp-algorithms.com/)
4. [古城算法 slides(google drive)](https://drive.google.com/drive/folders/17I-0mEeaY8X5j7RRMh0x_a2zNLu7jafq)
5. [输入数据规模和时间复杂度的关系](https://www.youtube.com/watch?v=eG99FDBeuJo)
6. [0x3ff-palindrome](https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/solutions/2569308/yu-chu-li-hui-wen-shu-zhong-wei-shu-tan-7j0zy/)