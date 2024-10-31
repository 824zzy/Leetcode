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
4. Maze: for this type of problems, it will always give you a matrix and you can only move right or down in the matrix
5. Time sequential: current state is only related to limited previous states
6. Time dependent: current state is related to all the previous states

## Matrix Exponentiation DP

``` py
MOD = 10**9 + 7

def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
   return [
         [sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
         for row in a
   ]

def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
   res = f0
   while n:
         if n & 1:
            res = mul(a, res)
         a = mul(a, a)
         n >>= 1
   return res
```

## Reference

- [leetcode|动态规划专项练习](https://zhuanlan.zhihu.com/p/84882320)
- [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)
