# Knapsack problem

There are two variants of knapsack problem, 0/1 knapsack problem and unbounded knapsack problem.

## 0/1 knapsack problem

In the case of 0/1 knapsack problem, we can either take an item or not. Thus in the code below, it is essentially a variant of time sequential template.

``` py
@cache
def dp(i):
    if CONDITION: return ?
    SKIP_ITEM
    TAKE_ITEM
    return ?(SKIP_ITEM, TAKE_ITEM)
```

## Unbounded knapsack problem

On the other hand, the unbounded knapsack problem remove the restriction that there is only one of each item.
Thus in the code below, it is essentially a variant of time dependent template.

```py
@cache
def dp(n):
    if n==0: return 0
    elif n<0: return inf
    return min(1+dp(n-c) for c in A)
```
