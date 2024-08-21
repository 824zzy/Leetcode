# Game Theory

Minimax: A decision rule used in decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case scenario. Originally formulated for two-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves.

## Template

``` py
@cache
def dp(i):
    if i == len(A):
        return 0
    for j in range(i, len(A)):
        ans = max(ans, A[i] - dp(j + 1))
    return ans
```