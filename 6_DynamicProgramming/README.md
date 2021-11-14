# Note

## Problem Solving Step

1. Split the original question into sub-questions
2. Confirm status
3. Confirm boundary conditions
4. Find state-transition equation

## Category

1. One Dimension
2. Two Dimension
   1. Longest Common Subsequence: 583, 1143
   2. Two pass for 4 directions: 542
3. LCS(Longest Common Subsequence)

## Kadane's algorithm

``` py
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

## Reference

- [leetcode|动态规划专项练习](https://zhuanlan.zhihu.com/p/84882320)
- [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)
