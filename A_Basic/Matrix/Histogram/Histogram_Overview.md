---
tags:
  - leetcode
  - basic
  - moc
---

# Histogram Model

## When to Use

| Problem Signal | Technique |
|---|---|
| Find largest rectangle in binary matrix | Histogram + monotonic stack (LC 85) |
| Count all rectangles in binary matrix | Histogram + monotonic stack (LC 1504) |
| Largest submatrix with column rearrangements | Histogram + sort each row (LC 1727) |
| Matrix has "continuous 1s" constraint per column | Histogram model reduces 2D to 1D per row |

## Core Idea

The histogram model compresses a 2D binary matrix into a 1D histogram for each row. Each histogram bar represents the number of continuous 1s ending at that row in that column. Once you have a histogram per row, you reduce matrix problems to histogram problems (usually LC 84 variants).

**Key insight:** For each row, treat it as the base of a histogram and solve "largest rectangle in histogram" (or counting/variant problems) on that 1D array.

## Template: Build Histogram Row-by-Row

```py
hist = [0] * len(A[0])

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]:
            hist[j] += 1
        else:
            hist[j] = 0
    # now hist[j] = number of consecutive 1s ending at row i, column j
    # solve 1D histogram problem on hist
```

## Connection to Classic Problems

### LC 84: Largest Rectangle in Histogram (base 1D problem)

Not included in this directory, but the histogram model reduces matrix problems to this. Given a histogram, find the largest rectangle area.

**Solution:** Use monotonic stack to find the next smaller element on left and right for each bar. For each bar as height, the width is `right - left - 1`.

```py
def largestRectangleArea(heights):
    n = len(heights)

    # next smaller on the right
    R = [n] * n
    stk = []
    for i in range(n):
        while stk and heights[stk[-1]] > heights[i]:
            R[stk.pop()] = i
        stk.append(i)

    # next smaller on the left
    L = [-1] * n
    stk = []
    for i in reversed(range(n)):
        while stk and heights[stk[-1]] >= heights[i]:
            L[stk.pop()] = i
        stk.append(i)

    # for each heights[i] as minimum height, find max rectangle
    ans = 0
    for i in range(n):
        ans = max(ans, heights[i] * (R[i] - L[i] - 1))
    return ans
```

### LC 85: Maximal Rectangle

Build histogram for each row, solve LC 84 on each histogram.

```py
def maximalRectangle(matrix):
    if not matrix: return 0
    ans = 0
    hist = [0] * len(matrix[0])

    for row in matrix:
        for j in range(len(row)):
            if row[j] == "1":
                hist[j] += 1
            else:
                hist[j] = 0
        ans = max(ans, largestRectangleArea(hist))
    return ans
```

### LC 1727: Largest Submatrix with Rearrangements

Build histogram for each row, but we can rearrange columns. So sort the histogram in descending order and compute max area.

```py
def largestSubmatrix(matrix):
    ans = 0
    hist = [0] * len(matrix[0])

    for row in matrix:
        for j in range(len(matrix[0])):
            if row[j]:
                hist[j] += 1
            else:
                hist[j] = 0

        # can rearrange columns, so sort descending
        sorted_hist = sorted(hist, reverse=True)
        for k, height in enumerate(sorted_hist):
            ans = max(ans, height * (k + 1))
    return ans
```

### LC 1504: Count Submatrices With All Ones

Build histogram for each row. For each histogram, count all rectangles bottom-right at each position using monotonic stack. This is a harder variant of LC 84.

**Key insight:** For position `j`, count how many rectangles end at `j`. Use a monotonic non-decreasing stack. When popping, adjust the count to reflect the lower height.

```py
def numSubmat(matrix):
    m, n = len(matrix), len(matrix[0])

    # build histogram in-place
    for i in range(m):
        for j in range(n):
            if matrix[i][j] and i > 0:
                matrix[i][j] += matrix[i - 1][j]

    ans = 0
    for i in range(m):
        stack = []  # mono-stack of non-decreasing height
        cnt = 0
        for j in range(n):
            # pop taller bars
            while stack and matrix[i][stack[-1]] > matrix[i][j]:
                jj = stack.pop()
                kk = stack[-1] if stack else -1
                # adjust count to reflect lower height
                cnt -= (matrix[i][jj] - matrix[i][j]) * (jj - kk)

            # add rectangles ending at j with height matrix[i][j]
            cnt += matrix[i][j]
            ans += cnt
            stack.append(j)

    return ans
```

## Related Patterns

### Maximal Square (LC 221, not histogram-based)

Maximal square is usually solved with DP, not histogram model. But you can also solve it with histogram + sliding window to enforce width = height.

**DP approach (simpler):**
```py
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

## LC References

| Problem | Difficulty | Key Insight |
|---|---|---|
| [LC 84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | L2 | Monotonic stack to find next smaller left/right |
| [LC 85: Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | L3 | Histogram + LC 84 for each row |
| [LC 1504: Count Submatrices With All Ones](https://leetcode.com/problems/count-submatrices-with-all-ones/) | L3 | Histogram + monotonic stack counting variant |
| [LC 1727: Largest Submatrix with Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) | L1 | Histogram + sort each row |
| [LC 221: Maximal Square](https://leetcode.com/problems/maximal-square/) | L1 | DP (not histogram-based, but related) |

## Key Insights

1. Histogram model converts 2D matrix problems into a series of 1D histogram problems.
2. For "maximum" problems, usually pair with monotonic stack (LC 84 pattern).
3. For "count all" problems, use monotonic stack with careful counting logic (LC 1504).
4. If you can rearrange columns, sort the histogram (LC 1727).
5. The histogram template is the same for all problems. The difference is what you do with each histogram.
6. Build histogram row-by-row (iterate top to bottom), not column-by-column.
