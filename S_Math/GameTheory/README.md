# Game Theory

## When to Use

| Problem Signal | Technique |
|---|---|
| Two players, alternating turns, perfect information, zero-sum | Minimax DP |
| Can pick from both ends of array | Interval minimax (dp[i][j]) |
| Can pick X items from current position | Linear minimax (dp[i]) |
| Constraint on how many items can be picked (e.g., M parameter) | Stateful minimax (dp[i][state]) |
| Pile game where you can remove 1, 2, 3, ... k stones | Nim game / Sprague-Grundy |
| Multiple independent piles, XOR wins | Nim game (XOR of pile sizes) |
| Mathematical pattern in winning positions | Closed-form solution (avoid DP) |
| Game tree with multiple independent subgames | Sprague-Grundy theorem (XOR of Grundy numbers) |

## Core Concept

Minimax is a decision rule used in two-player zero-sum games. The first player (Alice) maximizes their advantage, while the second player (Bob) minimizes it. Both players play optimally.

The key insight: `dp[state] = best_value_alice_can_get - best_value_bob_can_get`. Since Bob plays optimally against Alice's remaining choices, we have `dp[state] = max over all moves (value_of_move - dp[next_state])`.

## Template 1: Linear Minimax (Pick from Current Position)

Use when players can pick 1 or more consecutive items starting from the current position.

LC 1406, 1140, 1690, 1872

```py
# dp(i) = max net advantage when starting at position i
# net advantage = alice's gain - bob's gain
@cache
def dp(i):
    if i >= len(A):
        return 0
    ans = -inf
    for k in range(1, max_take + 1):  # can take 1, 2, ..., max_take items
        take = sum(A[i:i+k])  # or use prefix sum
        ans = max(ans, take - dp(i + k))
    return ans

# alice wins if dp(0) > 0
```

### With Prefix Sum

More efficient when calculating sums repeatedly.

```py
prefix = [0] + list(accumulate(A))

@cache
def dp(i):
    if i >= len(A):
        return 0
    ans = -inf
    for k in range(1, max_take + 1):
        take = prefix[min(i + k, len(A))] - prefix[i]
        ans = max(ans, take - dp(i + k))
    return ans
```

### With State Parameter (LC 1140)

When the number of items you can take depends on previous moves.

```py
@cache
def dp(i, M):  # M = max items can take divided by 2
    if i >= len(A):
        return 0
    ans = -inf
    take = 0
    for X in range(1, 2 * M + 1):  # can take 1 to 2*M items
        take += A[i + X - 1] if i + X - 1 < len(A) else 0
        ans = max(ans, take - dp(i + X, max(M, X)))
    return ans

# alice's score = (dp(0, 1) + sum(A)) // 2
# because: alice - bob = dp(0, 1) and alice + bob = sum(A)
```

## Template 2: Interval Minimax (Pick from Both Ends)

Use when players can pick from either end of the array.

LC 486, 877

```py
# dp(i, j) = max net advantage for subarray A[i..j]
@cache
def dp(i, j):
    if i > j:
        return 0
    # pick from left or right
    return max(A[i] - dp(i + 1, j), A[j] - dp(i, j - 1))

# alice wins if dp(0, len(A) - 1) >= 0
```

### Key Observations

- **Why subtract `dp(next_state)`?** Because after Alice picks, it's Bob's turn on the remaining array. Bob will maximize his own advantage, which is `-dp(next_state)` from Alice's perspective. So Alice's net gain is `value_picked - dp(next_state)`.

- **Converting net advantage to actual scores:** If `dp(0) = alice_score - bob_score` and `alice_score + bob_score = total_sum`, then `alice_score = (dp(0) + total_sum) // 2`.

- **Tie handling:** If `dp(0) == 0`, it's a tie. If `dp(0) > 0`, Alice wins. If `dp(0) < 0`, Bob wins.

## Template 3: Interval Minimax with Choice (LC 1563)

Use when players make choices that determine which subproblem to continue with.

```py
prefix = [0] + list(accumulate(A))

@cache
def dp(l, r):  # return max score for subarray A[l..r]
    if l == r:
        return 0
    ans = 0
    for m in range(l + 1, r + 1):  # split at m
        left_sum = prefix[m] - prefix[l]
        right_sum = prefix[r + 1] - prefix[m]
        if left_sum < right_sum:
            ans = max(ans, left_sum + dp(l, m - 1))
        elif left_sum > right_sum:
            ans = max(ans, right_sum + dp(m, r))
        else:
            ans = max(ans, left_sum + max(dp(l, m - 1), dp(m, r)))
    return ans
```

## Nim Game

Classic combinatorial game where two players alternately remove objects from piles. The player who takes the last object wins.

### Basic Nim (Single Pile, Remove 1-k Items)

LC 292

**Losing positions:** multiples of `k + 1`

```py
def canWin(n, k):
    return n % (k + 1) != 0
```

**Why?** If `n % (k + 1) == 0`, any move you make leaves the opponent at a non-multiple, from which they can return you to a multiple. You eventually reach n=0 (multiple) and lose.

### General Nim (Multiple Piles)

**Winning condition:** XOR of all pile sizes != 0

```py
def canWin(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return xor_sum != 0
```

If XOR is 0 (losing position), any move makes it non-zero (winning position for opponent). If XOR is non-zero, there exists a move to make it zero.

### Nim Variant (LC 1025)

Simple mathematical pattern recognition.

```py
def divisorGame(n):
    return n % 2 == 0
```

### Modulo Nim (LC 2029)

When stones are taken but the game depends on sum modulo k.

```py
cnt = Counter(x % 3 for x in stones)
# alice wins based on parity of cnt[0] and difference between cnt[1] and cnt[2]
if min(cnt[1], cnt[2]) == 0:
    return max(cnt[1], cnt[2]) > 2 and cnt[0] % 2 > 0
return abs(cnt[1] - cnt[2]) > 2 or cnt[0] % 2 == 0
```

## Sprague-Grundy Theorem

For game trees with multiple independent subgames, the Grundy number (nimber) of a position is the XOR of Grundy numbers of all subgames.

```py
@cache
def grundy(state):
    if is_losing_position(state):
        return 0
    # mex (minimal excludant) of all reachable states
    reachable = {grundy(next_state) for next_state in get_next_states(state)}
    mex = 0
    while mex in reachable:
        mex += 1
    return mex

# position is winning if grundy(initial_state) != 0
```

**Key properties:**
- Grundy number of a losing position is 0
- Grundy number of a position is the MEX (minimal excludant) of Grundy numbers of all positions reachable in one move
- For independent subgames, `grundy(game) = grundy(subgame1) ^ grundy(subgame2) ^ ...`

## Common Pitfalls

1. **Large n with simple pattern:** Some game theory problems have a closed-form solution (like LC 292). Always check if there's a mathematical pattern before writing DP, otherwise you'll TLE.

2. **Net advantage vs. actual scores:** The DP state represents `alice_score - bob_score`, not Alice's absolute score. To get actual scores, use `alice_score = (dp(0) + total_sum) // 2`.

3. **Forgetting the negative sign:** When recursing, you compute `value_picked - dp(next_state)`, not `value_picked + dp(next_state)`. The minus sign is because the opponent maximizes their own score, which hurts you.

4. **Interval DP boundary:** For `dp(i, j)`, the base case is `i > j` (empty range), not `i == j`.

5. **Prefix sum off-by-one:** When using prefix sum with `dp(i)`, remember that `prefix[0] = 0` and `prefix[i+1] - prefix[i]` gives `A[i]`.

## LeetCode Problems

| Problem | Difficulty | Pattern | Key Insight |
|---------|-----------|---------|-------------|
| [292. Nim Game](https://leetcode.com/problems/nim-game/) | L1 | Basic Nim | n % 4 != 0 (closed form) |
| [1025. Divisor Game](https://leetcode.com/problems/divisor-game/) | L0 | Math pattern | n % 2 == 0 (even always wins) |
| [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | L1 | Interval minimax | Pick from both ends |
| [877. Stone Game](https://leetcode.com/problems/stone-game/) | L1 | Interval minimax | Same as 486 |
| [1406. Stone Game III](https://leetcode.com/problems/stone-game-iii/) | L1 | Linear minimax | Take 1, 2, or 3 stones |
| [1690. Stone Game VII](https://leetcode.com/problems/stone-game-vii/) | L1 | Interval minimax | Score is sum of remaining |
| [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii/) | L2 | Stateful minimax | M parameter (can take 1 to 2M) |
| [1872. Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) | L2 | Linear minimax | Prefix sum mandatory |
| [1563. Stone Game V](https://leetcode.com/problems/stone-game-v/) | L3 | Interval minimax | Split array, O(n^3) optimization needed |
| [2029. Stone Game IX](https://leetcode.com/problems/stone-game-ix/) | L3 | Modulo Nim | Count mod 3, XOR-like parity logic |
