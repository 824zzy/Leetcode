---
tags:
  - leetcode
  - advanced
  - moc
---

# Sorting Algorithms

## When to Use

| Problem Signal | Technique |
|---|---|
| Find kth largest/smallest element | Quick Select (O(n) average) or Counting Sort (O(n) if range is small) |
| Count minimum swaps to sort | Cycle Sort |
| Maximum gap in sorted order (O(n)) | Bucket Sort with gap-sized buckets |
| Sort by frequency | Bucket Sort (group by count) or Counting Sort |
| Merge two sorted arrays | Merge Sort (two-pointer merge) |
| Sort array with O(n log n) worst case | Merge Sort |
| Range is small (max - min < 10^5) | Counting Sort (O(n + range)) |

## Quick Select

Hoare's selection algorithm. Finds the kth largest/smallest element in O(n) average time, O(n^2) worst case. Randomize input to avoid worst case.

Key insight: After partitioning around a pivot, recurse only into the side that contains the kth element.

### Template

```py
from random import shuffle

def findKthLargest(A, k):
    def partition(l, r):
        """Partition A[l:r] around A[l]. Return final position of pivot."""
        i, j = l + 1, r - 1
        while i <= j:
            if A[i] < A[l]:
                i += 1
            elif A[j] > A[l]:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j - 1
        A[l], A[j] = A[j], A[l]
        return j

    shuffle(A)  # avoid worst case
    l, r = 0, len(A)
    while True:
        m = partition(l, r)
        if m + k < len(A):
            l = m + 1
        elif m + k == len(A):
            return A[m]
        else:
            r = m
```

### LC References

- LC 215: Kth Largest Element in an Array
- LC 347: Top K Frequent Elements (apply after counting)
- LC 973: K Closest Points to Origin
- LC 1738: Find Kth Largest XOR Coordinate Value
- LC 1985: Find the Kth Largest Integer in the Array

## Counting Sort

Sort by counting occurrences of each value. O(n + range) time and space where range = max - min + 1.

Use when the range of values is small relative to n.

### Template

```py
def countingSort(A):
    mn, mx = min(A), max(A)
    cnt = [0] * (mx - mn + 1)

    for num in A:
        cnt[num - mn] += 1

    # reconstruct sorted array
    result = []
    for num in range(len(cnt)):
        result.extend([num + mn] * cnt[num])
    return result
```

### Kth largest with counting sort

```py
def findKthLargest(A, k):
    mn, mx = min(A), max(A)
    cnt = [0] * (mx - mn + 1)

    for num in A:
        cnt[num - mn] += 1

    rem = k
    for num in range(len(cnt) - 1, -1, -1):
        rem -= cnt[num]
        if rem <= 0:
            return num + mn
    return -1
```

### LC References

- LC 215: Kth Largest Element in an Array (when range is small)

## Bucket Sort

Group elements into buckets based on value range, then process buckets in order.

Key insight for maximum gap problem: If n numbers span [min, max], at least one gap is >= (max - min) / (n - 1). Use this as bucket size. The answer cannot be within a bucket, only between buckets.

### Template: Maximum Gap

```py
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    mn, mx = min(nums), max(nums)
    step = max(1, (mx - mn) // (len(nums) - 1))  # bucket size
    size = (mx - mn) // step + 1
    buckets = [[inf, -inf] for _ in range(size)]  # [min, max] in each bucket

    for num in nums:
        i = (num - mn) // step
        x, xx = buckets[i]
        buckets[i] = min(x, num), max(xx, num)

    ans = 0
    prev = mn
    for i in range(size):
        x, xx = buckets[i]
        if x < inf:  # bucket not empty
            ans = max(ans, x - prev)  # gap between buckets
            prev = xx
    return ans
```

### Template: Sort by frequency

```py
def frequencySort(s):
    cnt = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]

    for c, freq in cnt.items():
        buckets[freq].append(c)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for c in buckets[freq]:
            result.extend([c] * freq)
    return ''.join(result)
```

### LC References

- LC 164: Maximum Gap (O(n) via bucket sort)
- LC 347: Top K Frequent Elements (bucket by frequency)
- LC 451: Sort Characters By Frequency

## Cycle Sort

Counts the minimum number of swaps to sort an array by finding cycle lengths in the permutation.

Key insight: If element x should be at position mp[x], follow the cycle: x -> A[mp[x]] -> A[mp[A[mp[x]]]] -> ... until you return to x. A cycle of length k requires k-1 swaps.

### Template

```py
def cyclesort(A):
    mp = {x: i for i, x in enumerate(sorted(A))}
    seen = {x: False for x in A}
    ans = 0
    for i, x in enumerate(A):
        cnt = 0
        while i != mp[x] and not seen[x]:
            cnt += 1
            seen[x] = True
            i = mp[x]
            x = A[i]
        ans += max(0, cnt - 1)
    return ans
```

### LC References

- LC 2471: Minimum Number of Operations to Sort a Binary Tree by Level

## Merge Sort

Divide and conquer sorting algorithm. O(n log n) time, O(n) space. Stable sort.

### Template: Top-down recursive

```py
def mergeSort(A, p, r):
    """Sort A[p..r] in place."""
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
    return A

def merge(A, p, q, r):
    """Merge A[p..q] and A[q+1..r] in place."""
    n1, n2 = q - p + 1, r - q
    L = [A[p + i] for i in range(n1)] + [inf]
    R = [A[q + j + 1] for j in range(n2)] + [inf]
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
```

### Template: Two-pointer merge (already sorted arrays)

```py
def merge(A, B):
    """Merge two sorted arrays."""
    ans = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            ans.append(A[i])
            i += 1
        else:
            ans.append(B[j])
            j += 1
    ans.extend(A[i:])
    ans.extend(B[j:])
    return ans
```

### LC References

- LC 912: Sort an Array
- LC 2570: Merge Two 2D Arrays by Summing Values

## Reference

1. [Cycle Sort](https://www.geeksforgeeks.org/cycle-sort/)
