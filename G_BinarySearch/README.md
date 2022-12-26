# Binary Search

Binary search algorithm can be applied iff the array has **monotonicity**。

A few signal that indicates a problem is a binary search problem:

1. The problem asks for the mini-max or max-mini
2. The array is sorted

## Basic Template

``` py
def binary_search(self, A: List[int], t: int) -> int:
      l, r = 0, len(A)
      while l<r:
            m = (l+r)//2
            if A[m]>t: r = m
            else: l = m + 1
      return l
```

## Bisect Module

1. insort: `insort(list, num)`, `insort_left(list, num)` and `insort_right(list, num)`: Insert num in a list. If list has repeat value, insort_left and insort_right will insert num in different position.

2. bisect: `bisect(list, num)`, `bisect_left(list, num)` and `bisect_right(list, num)`: find the location where the value will be inserted and return without inserting.

## Reference

- [[Python] Powerful Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/study-guide/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
