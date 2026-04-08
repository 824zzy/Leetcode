---
tags:
  - leetcode
  - math
  - moc
---

# Bezout's Lemma

## Definition

Let $a, b$ be integers, not both zero. Then there exist integers $x, y$ such that $ax + by = \gcd(a, b)$.

## When to Use

| Problem Signal | Technique |
|---|---|
| Check if linear combination equals target | GCD test: possible iff target % gcd(a, b) == 0 |
| Check if sum can equal 1 (select/multiply elements) | GCD test: possible iff gcd(all elements) == 1 |
| Find cycle length in circular array transformations | gcd(n, k) determines the period |
| Grouping elements by modular arithmetic cycles | Elements repeat every gcd(n, k) positions |

## Key Insight

The set of all integer linear combinations of $a$ and $b$ is exactly the set of all multiples of $\gcd(a, b)$.

In other words, $ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$.

## Extended GCD

Finds integers $x, y$ such that $ax + by = \gcd(a, b)$.

```py
def extended_gcd(a, b):
    """Returns (gcd, x, y) where ax + by = gcd"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# usage: find one solution to ax + by = c
g, x0, y0 = extended_gcd(a, b)
if c % g != 0:
    # no solution
    pass
else:
    # one solution: (x0 * c/g, y0 * c/g)
    x = x0 * (c // g)
    y = y0 * (c // g)
```

## Linear Diophantine Equation

$ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$.

If one solution $(x_0, y_0)$ is known, the general solution is:

$$x = x_0 + \frac{b}{\gcd(a, b)} \cdot t$$
$$y = y_0 - \frac{a}{\gcd(a, b)} \cdot t$$

where $t$ is any integer.

## Common Patterns

### Pattern 1: Check if sum of subset can equal target

LC 1250

If you can select elements from array $A$ and multiply each by an integer coefficient to get sum $= k$, then $k$ must be divisible by $\gcd(A)$.

```py
def isGoodArray(self, nums: List[int]) -> bool:
    # can we get sum = 1?
    return gcd(*nums) == 1
```

### Pattern 2: Circular array transformation period

LC 2607

If operation shifts by $k$ in an array of size $n$, the cycle length is $\gcd(n, k)$. Elements repeat every $\gcd(n, k)$ positions.

```py
def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
    # bezout's lemma to find repeat cycle length
    k = gcd(k, len(arr))
    ans = 0
    for i in range(k):
        # grouping: elements i, i+k, i+2k, ... must be equal
        group = sorted(arr[i::k])
        # greedy: set all to median minimizes cost
        median = group[len(group) // 2]
        ans += sum(abs(x - median) for x in group)
    return ans
```

## LeetCode References

- LC 1250: Check If It Is a Good Array
- LC 2607: Make K-Subarray Sums Equal

## Reference

- [裴蜀定理 (OI Wiki)](https://oi-wiki.org/math/number-theory/bezouts/)
