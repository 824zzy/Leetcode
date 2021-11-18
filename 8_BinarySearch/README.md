# Note

## Template

``` py
def binary_search(self, A: List[int], t: int) -> int:
      l, r = 0, len(A)-1
      while l<=r:
            m = (l+r)//2
            if A[m]==t: return m
            if A[m]<t: l = m + 1
            else: r = m - 1
      return -1
```

## Tips

1. Reverse a list sometime useful.

## Reference

- [[Python] Powerful Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/study-guide/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
