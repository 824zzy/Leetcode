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
4. Can I enumerate on specific variable?
5. Can I use two passes?
6. Can I solve it reversely?
7. Can I convert the problem to a other problem?
8. "Subarray" ==> sliding window, monotonic stack/queue
9. "Sum" ==> prefix sum

## Cheat sheet


### Palindrome
Efficiently find all the palindrome numbers in a range 10**9:

```py
pal = []
base = 1
while base <= 10000: # 
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