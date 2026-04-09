# Backtracking

## When to Use

| Problem Signal | Technique |
|---|---|
| Generate all subsets / combinations | Array backtracking (subsets pattern) |
| Generate all permutations | Array backtracking (permutations pattern) |
| Generate all valid parentheses / bracket sequences | Array backtracking with balance tracking |
| Partition array/string into valid parts | Array backtracking (partition pattern) |
| Find/count all paths in a grid | Graph backtracking with visited tracking |
| Place items on grid with constraints (N-Queens, Sudoku) | Graph backtracking with conflict checking |
| Find word in grid (Word Search) | Graph backtracking with cell marking |
| Find all root-to-leaf paths / tree structure | Tree backtracking with path tracking |
| Generate all valid BSTs / expressions | Divide and conquer with recursive construction |
| Partition items into K groups (jobs, subsets) | Array backtracking with optimization pruning |
| Count duplicates in input | Sort first, then skip duplicates during iteration |

## Array Backtracking

Key insight: explore all ways to build a solution incrementally, backtrack when constraints are violated.

### Template: Subsets / Combinations

Use when you need all subsets or combinations of size k. Each element is either included or excluded.

```py
ans = []
stk = []

def dfs(i):
    if CONDITION:
        ans.append(stk.copy())
        return
    for j in range(i, len(A)):
        stk.append(A[j])
        dfs(j + 1)  # j+1 ensures no reuse
        stk.pop()

dfs(0)
return ans
```

LC 78 (subsets), 77 (combinations), 39 (combination sum), 216 (combination sum III)

**With duplicates:** Sort first, skip duplicate elements at same recursion level.

```py
A.sort()
def dfs(i, ...):
    for j in range(i, len(A)):
        if j > i and A[j] == A[j - 1]:
            continue  # skip duplicate at this level
        stk.append(A[j])
        dfs(j + 1, ...)
        stk.pop()
```

LC 40 (combination sum II), 90 (subsets II)

### Template: Permutations

Use when order matters and each element must be used exactly once.

```py
ans = []
stk = []

def dfs(remaining):
    if not remaining:
        ans.append(stk.copy())
        return
    for i, x in enumerate(remaining):
        stk.append(x)
        dfs(remaining[:i] + remaining[i + 1:])
        stk.pop()

dfs(A)
return ans
```

LC 46 (permutations), 784 (letter case permutation)

**With duplicates:** Sort first, track which indices are used to avoid symmetric duplicates.

```py
A.sort()
ans = []
stk = []

def dfs(seen):
    if len(stk) == len(A):
        ans.append(stk.copy())
        return
    for i, x in enumerate(A):
        if i not in seen:
            # skip if same value as previous and previous not used
            if i > 0 and A[i] == A[i - 1] and i - 1 not in seen:
                continue
            stk.append(x)
            dfs(seen | {i})
            stk.pop()

dfs(set())
return ans
```

LC 47 (permutations II)

### Template: Partition / Split

Use when splitting an array or string into valid parts (palindromes, valid numbers, etc.).

```py
ans = []
stk = []

def dfs(i):
    if i == len(A):
        ans.append(stk.copy())
        return
    for j in range(i + 1, len(A) + 1):
        if is_valid(A[i:j]):
            stk.append(A[i:j])
            dfs(j)
            stk.pop()

dfs(0)
return ans
```

LC 131 (palindrome partitioning), 93 (restore IP addresses), 140 (word break II)

**Binary choice style:** At each position, decide whether to cut or continue.

```py
def dfs(i, current_part):
    if i == len(A):
        if is_valid(current_part):
            stk.append(current_part)
            ans.append(stk.copy())
            stk.pop()
        return
    # cut here (if current part is valid)
    if current_part and is_valid(current_part):
        stk.append(current_part)
        dfs(i + 1, A[i])
        stk.pop()
    # don't cut, extend current part
    dfs(i + 1, current_part + A[i])
```

LC 131 (palindrome partitioning, alternative approach)

### Template: Generate valid sequences

Use for problems like generating valid parentheses where you track state (e.g., balance, remaining quota).

```py
ans = []
stk = []

def dfs(state_params):
    if GOAL_STATE:
        ans.append(''.join(stk))
        return
    if can_add_option_1:
        stk.append(option_1)
        dfs(updated_state_1)
        stk.pop()
    if can_add_option_2:
        stk.append(option_2)
        dfs(updated_state_2)
        stk.pop()

dfs(initial_state)
return ans
```

LC 22 (generate parentheses), 320 (generalized abbreviation), 1980 (find unique binary string)

**Example (parentheses):**

```py
def dfs(left_remaining, right_open):
    if left_remaining == 0 and right_open == 0:
        ans.append(''.join(stk))
        return
    if left_remaining > 0:
        stk.append('(')
        dfs(left_remaining - 1, right_open + 1)
        stk.pop()
    if right_open > 0:
        stk.append(')')
        dfs(left_remaining, right_open - 1)
        stk.pop()
```

## Graph Backtracking

Key insight: mark cells as visited during recursion, restore when backtracking.

### Template: Grid exploration

Use for finding paths, searching words, or exploring reachable cells in a grid.

```py
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, state):
    if CONDITION:
        return RESULT

    tmp = A[x][y]
    A[x][y] = '#'  # mark as visited

    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and A[nx][ny] != '#' and OTHER_CONDITIONS:
            result = dfs(nx, ny, updated_state)
            if result:  # early return if found
                A[x][y] = tmp
                return result

    A[x][y] = tmp  # restore
    return RESULT

# try all starting positions
for i in range(M):
    for j in range(N):
        if START_CONDITION:
            if dfs(i, j, initial_state):
                return ANSWER
```

LC 79 (word search), 212 (word search II), 980 (unique paths III)

**When to use visited set vs. marking in place:**
- Mark in place (`A[x][y] = '#'`) when the grid is char-based and '#' is not in the input
- Use visited set (`visited.add((x, y))`) when you need to restore original values or grid contains all possible markers

### Template: Constraint placement

Use for placing items on a grid with conflict constraints (N-Queens, Sudoku).

```py
def dfs(row):
    if row == N:
        ans.append(construct_solution())
        return

    for col in range(N):
        if is_valid(row, col):  # check constraints
            place(row, col)
            mark_conflicts(row, col)
            dfs(row + 1)
            unmark_conflicts(row, col)
            remove(row, col)

dfs(0)
return ans
```

LC 51 (N-Queens), 52 (N-Queens II), 37 (Sudoku solver)

**N-Queens conflict tracking:**

```py
cols = set()
left_diag = set()   # row + col
right_diag = set()  # row - col

def dfs(row):
    if row == n:
        ans.append(construct_board())
        return
    for col in range(n):
        if col not in cols and row + col not in left_diag and row - col not in right_diag:
            board[row][col] = 'Q'
            cols.add(col)
            left_diag.add(row + col)
            right_diag.add(row - col)
            dfs(row + 1)
            board[row][col] = '.'
            cols.remove(col)
            left_diag.remove(row + col)
            right_diag.remove(row - col)
```

## Tree Backtracking

Key insight: pass path down through recursion or use a stack with proper push/pop.

### Template: Root-to-leaf paths

Use when collecting all paths from root to leaves.

```py
ans = []
stk = []

def dfs(node, accumulated_state):
    if not node:
        return

    stk.append(node.val)

    if not node.left and not node.right:  # leaf
        if CONDITION(accumulated_state):
            ans.append(stk.copy())
    else:
        dfs(node.left, updated_state)
        dfs(node.right, updated_state)

    stk.pop()  # backtrack

dfs(root, initial_state)
return ans
```

LC 113 (path sum II), 257 (binary tree paths), 988 (smallest string starting from leaf)

**Alternative: pass path as parameter (no explicit backtracking needed):**

```py
def dfs(node, path):
    if not node:
        return
    new_path = path + [node.val]
    if not node.left and not node.right:
        if CONDITION:
            ans.append(new_path)
        return
    dfs(node.left, new_path)
    dfs(node.right, new_path)
```

LC 113 (path sum II, alternative)

## Divide and Conquer

Key insight: split problem into independent subproblems, combine results from all possibilities.

### Template: Generate all structures

Use when constructing all valid trees or evaluating all ways to parse an expression.

```py
@cache
def dc(left, right):
    if left >= right:
        return [BASE_CASE]

    results = []
    for split in range(left, right):
        for left_result in dc(left, split):
            for right_result in dc(split + 1, right):
                results.append(combine(left_result, right_result))

    return results

return dc(0, n)
```

LC 95 (unique BST II), 241 (different ways to add parentheses)

**Example (BST generation):**

```py
@cache
def dfs(l, r):
    if l == r:
        return [None]
    ans = []
    for i in range(l, r):
        for left_tree in dfs(l, i):
            for right_tree in dfs(i + 1, r):
                ans.append(TreeNode(i, left_tree, right_tree))
    return ans

return dfs(1, n + 1)
```

LC 95 (unique BST II)

**Example (expression evaluation):**

```py
def dc(l, r):
    if l == r:
        return [int(tokens[l])]

    results = []
    for i in range(l, r):
        if tokens[i] in operators:
            for left_val in dc(l, i - 1):
                for right_val in dc(i + 1, r):
                    results.append(apply(tokens[i], left_val, right_val))
    return results
```

LC 241 (different ways to add parentheses)

## Optimization and Pruning

Pruning can reduce exponential complexity by orders of magnitude.

### 1. Sort first

Sorting enables early termination when remaining elements can't satisfy constraints.

```py
A.sort()  # or A.sort(reverse=True) for largest-first

def dfs(i, remaining):
    if remaining < 0:
        return  # prune: can't satisfy
    if sum(A[i:]) < remaining:
        return  # prune: not enough left
    # continue search
```

LC 40 (combination sum II), 698 (partition to K equal sum subsets)

### 2. Skip duplicates at same level

After sorting, avoid exploring symmetric branches.

```py
for j in range(i, len(A)):
    if j > i and A[j] == A[j - 1]:
        continue  # skip duplicate at this recursion level
    # process A[j]
```

LC 40 (combination sum II), 47 (permutations II), 90 (subsets II)

### 3. Track and prune based on current best

For optimization problems, prune branches that can't improve the current answer.

```py
self.best = initial_value

def dfs(i, current_state):
    if i == n:
        self.best = optimize(self.best, current_state)
        return
    for choice in choices:
        if is_worse_than_current_best(choice):
            continue  # prune
        apply(choice)
        dfs(i + 1, updated_state)
        undo(choice)
```

LC 1723 (find minimum time to finish all jobs), 473 (matchsticks to square)

**Example (minimize maximum load):**

```py
A.sort(reverse=True)  # assign large jobs first
self.ans = sum(A)
buckets = [0] * k

def dfs(i):
    if i == len(A):
        self.ans = min(self.ans, max(buckets))
        return
    for j in range(k):
        if buckets[j] + A[i] < self.ans:  # prune if already worse
            buckets[j] += A[i]
            dfs(i + 1)
            buckets[j] -= A[i]
        if buckets[j] == 0:
            break  # no point assigning to other empty buckets
```

LC 1723 (find minimum time to finish all jobs)

### 4. Break symmetry

For partitioning problems, avoid assigning items to equivalent buckets.

```py
for j in range(k):
    buckets[j] += A[i]
    dfs(i + 1)
    buckets[j] -= A[i]
    if buckets[j] == 0:
        break  # all empty buckets are equivalent
```

LC 698 (partition to K equal sum subsets), 1723 (find minimum time to finish all jobs)

## Choosing the Right Approach

**Array backtracking vs. DP:**
- Use backtracking when you need to generate all solutions (subsets, permutations)
- Use DP when you only need to count solutions or find one optimal solution

**Backtracking vs. BFS:**
- Use backtracking when the state space has complex constraints (N-Queens, Sudoku)
- Use BFS when you need shortest path in unweighted graphs

**Mark in place vs. visited set:**
- Mark in place (`A[x][y] = '#'`) for simple grid problems (word search)
- Visited set for multi-path tracking or when you can't modify the grid

**Sort vs. no sort:**
- Sort when you have duplicates or need pruning based on remaining elements
- Don't sort when order matters (permutations) or duplicates don't exist

## Common Pitfalls

1. **Forgetting to copy:** Use `ans.append(stk.copy())` not `ans.append(stk)`
2. **Wrong duplicate skip:** `if j > i and A[j] == A[j-1]` not `if j > 0 and A[j] == A[j-1]`
3. **Forgetting to restore:** Always restore state after recursion (pop from stack, unmark visited)
4. **Reusing elements:** For combinations, use `dfs(j + 1)` not `dfs(j)` to avoid reuse
5. **Base case before action:** Check base case before taking action (placing queen, marking cell)

## Time Complexity

- Subsets: O(2^n * n) for n elements
- Permutations: O(n! * n) for n elements
- Combinations: O(C(n,k) * k) for choosing k from n
- N-Queens: O(n!) with pruning
- Partition into K groups: O(k^n) worst case, much better with pruning
- Grid search: O(3^L) for path of length L (3 choices per step after initial)
